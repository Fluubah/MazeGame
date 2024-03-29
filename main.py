import pygame
import sys


pygame.init()
Bfont = pygame.font.Font('NimbusSanL-Reg.otf', 30)


map1=[
    [4],
    [2,0,0,1],
    [1,1,0,1],
    [0,0,0,1],
    [3,1,1,1]
    ]

map2=[
    [8],
    [1,1,1,1,1,0,0,0],
    [1,2,0,0,1,0,1,0],
    [1,1,1,0,1,0,1,0],
    [1,1,1,0,0,0,1,0],
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,0,0,0],
    [1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,3,1]
    ]
map3=[
    [8],
    [2,0,1,1,1,0,0,0],
    [1,0,1,0,0,0,1,0],
    [1,0,0,0,1,0,1,0],
    [1,1,1,1,1,0,1,0],
    [1,0,0,0,0,0,1,0],
    [1,0,1,1,1,1,1,0],
    [1,0,0,0,0,1,0,0],
    [1,0,1,1,0,1,3,1]
    ]
map4=[
    [8],
    [1,1,1,1,1,1,3,1],
    [1,1,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,1,1,0,1,0,1],
    [1,0,1,2,0,1,0,1],
    [1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]
    ]
map5=[
    [4],
    [1,1,1,1],
    [1,2,1,1],
    [1,1,3,1],
    [1,1,1,1]
    ]
maps=[map1,map2,map3, map4, map5]


current_map=0
mapsize=maps[current_map][0][0]
maps[current_map].pop(0)
screen_width=800
screen_height=800
tilesize=screen_width/mapsize
time=11*60
timeleft=time

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze")
doneex=False
def changemap():
    global mapsize
    global current_map
    global tilesize
    global maps
    current_map+=1
    mapsize=maps[current_map][0][0]
    tilesize=screen_width/mapsize
    maps[current_map].pop(0)
    print(maps[current_map])


def draw_map(map):
    for col in range(mapsize):

        for row in range(mapsize):

            if map[col][row] == 0 and PlayerO.started:
                color=(100,100,100)
                Wall(color, row*tilesize, col*tilesize, tilesize-2)
            elif map[col][row]==1 and PlayerO.started:
                color=(255,255,255)
                Wall(color, row*tilesize, col*tilesize, tilesize-2)
            elif map[col][row]==2:
                color=(0,0,255)
                Wall(color, row*tilesize, col*tilesize, tilesize-2)
            elif map[col][row]==3 and PlayerO.started:
                color=(0,255,0)
                Wall(color, row*tilesize, col*tilesize, tilesize-2)
            else:
                color=(0,0,0)
                Wall(color, row*tilesize, col*tilesize, tilesize-2)
        # pygame.draw.rect(screen, color, (row*tilesize, col*tilesize, tilesize-2, tilesize-2))           


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super(Explosion, self).__init__()
        self.index = 0
        self.frames=["frame_00_delay-0.1s.gif","frame_01_delay-0.1s.gif","frame_02_delay-0.1s.gif","frame_03_delay-0.1s.gif","frame_04_delay-0.1s.gif","frame_05_delay-0.1s.gif","frame_06_delay-0.1s.gif","frame_07_delay-0.1s.gif"]
        self.x = x
        self.done=False
        self.y = y
        self.images = [pygame.image.load(filename).convert_alpha() for filename in self.frames]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center = (x,y))
    def animate(self):
        if self.index<len(self.frames)-1:
            self.index+=1
            self.images = [pygame.image.load(filename).convert_alpha() for filename in self.frames]
            self.image = self.images[self.index]
            self.rect = self.image.get_rect(center = (self.x,self.y))
        else:
            self.done=True

class Wall(pygame.sprite.Sprite):
    def __init__(self, color, x, y, size):
        super(Wall, self).__init__()
        self.x = x
        self.y = y
        self.color = color
        pygame.draw.rect(screen, color, (x, y, size, size))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.x, self.y = pygame.mouse.get_pos()
        self.radius = 10
        self.color = (0,0,0)
        self.started=False

        self.image = pygame.Surface((self.radius*2, self.radius*2),pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()

        pygame.draw.circle(self.image, (0,0,0), (self.x, self.y), self.radius)
        self.rect = self.image.get_rect(center = (self.x,self.y))
    def move(self):
        self.x, self.y = pygame.mouse.get_pos()

    def check(self):
        global doneex
        global e
        global timeleft
        if maps[current_map][int(self.y/tilesize)][int(self.x/tilesize)] == 2:
            self.started=True
        if maps[current_map][int(self.y/tilesize)][int(self.x/tilesize)] == 1 or (self.x > screen_width) or (self.x<0) or (self.y>screen_height) or (self.y<0):
            if self.started:
                EXP.add(Explosion(self.x,self.y))
            self.started=False
            timeleft=time
        if self.started and maps[current_map][int(self.y/tilesize)][int(self.x/tilesize)] == 3 and e<1:
            self.started=False
            changemap()
            timeleft=time



players = pygame.sprite.Group()
PlayerO = Player()
players.add(PlayerO)
EXP = pygame.sprite.Group()
clock = pygame.time.Clock()
running=True
e=0
while running:
    e-=1
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running=False
    screen.fill((0,0,0))
    draw_map(maps[current_map])
    players.draw(screen)
    for i in EXP:
        i.animate()
        if i.done==False:
            EXP.draw(screen)
    for player in players:
        player.move()
        player.check()
    if PlayerO.started:
        timeleft-=1
        text=str(int(timeleft//60))
        text = Bfont.render(text, True, (0,0,255))
        screen.blit(text, (400, 400))
        if timeleft == 0:
            PlayerO.started=False
            timeleft=time
    if PlayerO.started == False:
        PlayerO.started=False
        text = Bfont.render("Put your mouse on the blue to start the countdown", True, (0,0,255))
        text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(text, text_rect)
    # Fill the screen with a color (e.g., white)


    pygame.display.flip()


    clock.tick(60)

pygame.quit()
sys.exit()