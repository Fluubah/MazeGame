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

def changemap():
    print("ah")
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
            elif map[col][row]==1 and PlayerO.started:
                color=(255,255,255)
            elif map[col][row]==2:
                color=(0,0,255)
            elif map[col][row]==3 and PlayerO.started:
                color=(0,255,0)
            else:
                color=(0,0,0)
            pygame.draw.rect(screen, color, (row*tilesize, col*tilesize, tilesize-2, tilesize-2))

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
        global e
        global timeleft
        if maps[current_map][int(self.y/tilesize)][int(self.x/tilesize)] == 2:
            self.started=True
        if maps[current_map][int(self.y/tilesize)][int(self.x/tilesize)] == 1 or (self.x > screen_width) or (self.x<0) or (self.y>screen_height) or (self.y<0):
            self.started=False
            timeleft=time
        if self.started and maps[current_map][int(self.y/tilesize)][int(self.x/tilesize)] == 3 and e<1:
            self.started=False
            changemap()
            timeleft=time



players = pygame.sprite.Group()
PlayerO = Player()
players.add(PlayerO)

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
    for player in players:
        player.move()
        player.check()
    if PlayerO.started:
        timeleft-=1
        text=str(int(timeleft//60))
        text = Bfont.render(text, True, (0,0,255))
        screen.blit(text, (400, 400))
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