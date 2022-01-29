import pygame
from Character import *
from Beat import *

characterList = []

playerCharacterA = character(vec2D(100,100), 10, (255,0,0), 10, 100, 10, 1)
playerCharacterB = character(vec2D(100,150), 10, (0,255,0), 10, 100, 10, 1)
playerCharacterC = character(vec2D(150,100), 10, (0,0,255), 10, 100, 10, 1)

characterB = character(vec2D(300,200), 20, (125, 125, 0), 3, 100, 1, 0)
characterC = character(vec2D(200,200), 20, (0,125, 255), 3, 20, 1, 0)
characterD = character(vec2D(300,300), 20, (125,0, 125), 3, 50, 1, 0)
playerList = [playerCharacterA, playerCharacterB, playerCharacterC]
enemyList = [characterB, characterC, characterD]

pygame.init()
screen = pygame.display.set_mode([800,600])
barSurface = pygame.Surface((200,600))
flag = True

white = [255,255,255]
#green = [0,255,0]
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
beatList = list()
beatList.append(beat.load(timerObj, pygame.mixer.Sound('incredibox/V1/01.BEATS 1.mp3'), 'beat1.txt'))
beatList.append(beat.load(timerObj, pygame.mixer.Sound('incredibox/V1/06.EFFECTS 1.mp3'), 'beat2.txt'))
beatList.append(beat.load(timerObj, pygame.mixer.Sound('incredibox/V1/11.MELODIES 1.mp3'), 'beat3.txt'))
beatList.append(beat.makeFromBpm(timerObj, 250, bpm*3, pygame.mixer.Sound('incredibox/V1/11.MELODIES 1.mp3')))
#beatList.append(beat.makeFromBpm(timerObj, 250, bpm*4, pygame.mixer.Sound('incredibox/V1/16.VOICES 1.mp3')))
#beatList.append(beat.load(timerObj, pygame.mixer.Sound('incredibox/V1/01.BEATS 1.mp3'), 'beat.txt'))
for beatI in beatList:
    timerObj.attach(beatI)

running = True
barPrev = pygame.time.get_ticks()
rectI=0
screenFlag = False
beatFlags = [False, False, False, False]
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            raise SystemExit
    if pygame.time.get_ticks()-barPrev>timerObj.beatMs:
        barPrev = pygame.time.get_ticks()
        rectI+=1
        rectI%=250
        beatResults = timerObj.moveOneBar()
        flag = beatResults[0]
        if flag:
            screenFlag = not screenFlag
            #beatList[0].soundObj.play()
        beatFlags = beatResults
    for beatI in range(len(beatList)):
        barRect = pygame.Rect(200/len(beatList)*beatI+2, 0, 200/len(beatList)-4, 600)
        barSurface.fill(color = (125,125,125), rect=barRect)
        for i in range(250):
            idx = (timerObj.beatBarIdx[0]+i)%beatList[beatI].beatN
            barRect = pygame.Rect(200/len(beatList)*beatI+2, 600-i*(600/beatList[beatI].beatN), 200/len(beatList)-4, (600/beatList[beatI].beatN))
            if beatList[beatI].beatBars[idx]==True:
                if idx==0:
                    barSurface.fill(color = (255,0,0),rect=barRect)
                else:
                    barSurface.fill(color = (255,255,0),rect=barRect)
        if timerObj.beatBarIdx[beatI]==0:
            beatList[beatI].soundObj.stop()
            beatList[beatI].soundObj.play()

    screen.fill(white)
        
    screen.blit(barSurface, (600,0))
    i=0
    for playableCharacterI in playerList:
        playableCharacterI.update(screen, enemyList, beatFlags[i])
        i+=1
    for characterI in enemyList:
        characterI.update(screen, playerList, flag)
        if characterI.health<=0:
            enemyList.remove(characterI)
    pygame.display.update()
    pygame.display.flip()
