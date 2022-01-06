import pygame
from Character import *
from Beat import *

characterList = []

characterA = character(vec2D(100,100), 10, (255,0,0), 10, 100, 10, 1)
characterB = character(vec2D(300,200), 20, (0,0,255), 3, 100, 1, 0)
characterC = character(vec2D(200,200), 20, (0,125, 255), 3, 20, 1, 0)
characterD = character(vec2D(300,300), 20, (125,0, 125), 3, 50, 1, 0)
enemyList = [characterB, characterC, characterD]

pygame.init()
screen = pygame.display.set_mode([800,600])
barSurface = pygame.Surface((800,50))
flag = True

white = [255,255,255]
green = [0,255,0]
bpm = int(input())

print(60000/bpm)

'''barN = 200
barLenTime = 4000
bar = [False]*barN
#200(bar) = 4000(ms)
barMs = barLenTime/barN
print(60000/bpm)
print((60000/bpm)/barMs)
for i in range(barN):
    if barMs*i%int(60000/bpm)==0:
        bar[i] = True
print(bar)'''

timerObj = timer(20)
beatObj = beat.makeFromBpm(timerObj, 200, bpm, None)
timerObj.attach(beatObj)

running = True
barPrev = pygame.time.get_ticks()
rectI=0
screenFlag = False
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            raise SystemExit
    if pygame.time.get_ticks()-barPrev>timerObj.beatMs:
        barPrev = pygame.time.get_ticks()
        rectI+=1
        rectI%=200
        beatResults = timerObj.moveOneBar()
        flag = beatResults[0]
        if flag:
            screenFlag = not screenFlag
            beatObj.soundObj.play()
    for i in range(200):
        idx = (timerObj.beatBarIdx[0]+i)%beatObj.beatN
        barRect = pygame.Rect(i*(800/beatObj.beatN), 0, (800/beatObj.beatN), 50)
        if beatObj.beatBars[idx]==True:
            barSurface.fill(color = (255,255,0),rect=barRect)
        else:
            barSurface.fill(color = (125,125,125), rect=barRect)

    if screenFlag:
        screen.fill(white)
        
    else:
        screen.fill(green)
        
    screen.blit(barSurface, (0,0))
    characterA.update(screen, enemyList, flag)
    for characterI in enemyList:
        characterI.update(screen, [characterA], flag)
        if characterI.health<=0:
            enemyList.remove(characterI)
    pygame.display.update()
    pygame.display.flip()
