import pygame
import sys


pygame.init()


map1=[
    [4],
    [2,0,0,1],
    [1,1,0,1],
    [0,0,0,1],
    [0,1,1,1]
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
    [1,0,1,1,1,1,1,1]
]


maps=[map1,map2]


current_map=0
mapsize=maps[current_map][0][0]
maps[current_map].pop(0)
print(maps[current_map])
screen_width=800
screen_height=800
tilesize=screen_width/mapsize


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze")

def changemap():
    print("ah")
    global mapsize
    global current_map
    global tilesize
    global maps
    print(current_map)
    current_map+=1
    mapsize=maps[current_map][0][0]
    tilesize=screen_width/mapsize
    maps[current_map].pop(0)
    print(maps[current_map])


def draw_map(map):
    for col in range(mapsize):

        for row in range(mapsize):

            if map[col][row] == 0:
                color=(100,100,100)
            elif map[col][row]==1:
                color=(255,255,255)
            elif map[col][row]==2:
                color=(0,255,0)
            pygame.draw.rect(screen, color, (row*tilesize, col*tilesize, tilesize-2, tilesize-2))

class Player():
    def __init__(self):
        super(Player, self).__init__()
        self.x, self.y = pygame.mouse.get_pos()

        def move(self):
            self.x, self.y = self.x, self.y = pygame.mouse.get_pos()
            print(self.x, self.y)


players = pygame.Group()

players.add(Player)
clock = pygame.time.Clock()
running=True
e=0
while running:
    e-=1
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and e < 1:
        e=10
        changemap()
        

    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running=False
    screen.fill((0,0,0))
    draw_map(maps[current_map])
    for Player in players:
        Player.move()

    # Fill the screen with a color (e.g., white)


    pygame.display.flip()


    clock.tick(60)

pygame.quit()
sys.exit()