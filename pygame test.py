import pygame, sys
import time
pygame.init()
screen = pygame.display.set_mode([800,600])
barSurface = pygame.Surface((800,50))
flag = True
white = [255,255,255]
red = [255,0,0]
bpm = int(input())

print(60000/bpm)

barN = 200
barLenTime = 4000
bar = [False]*barN
#200(bar) = 4000(ms)
barMs = barLenTime/barN
print(60000/bpm)
print((60000/bpm)/barMs)
for i in range(barN):
    if barMs*i%int(60000/bpm)==0:
        bar[i] = True
print(bar)

rectI = 0

running = True
prev = pygame.time.get_ticks()
barPrev = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    '''if pygame.time.get_ticks()-prev>60000/bpm:
        prev = pygame.time.get_ticks()
        if flag:
            screen.fill(white)
            flag = False
        else:
            screen.fill(red)
            flag = True
            soundObj = pygame.mixer.Sound('drum.mp3')
            soundObj.play()'''
    if pygame.time.get_ticks()-barPrev>barMs:
        barPrev = pygame.time.get_ticks()
        rectI+=1
        rectI%=200
        if bar[rectI]==True:
            if flag:
                screen.fill(white)
                flag = False
            else:
                screen.fill(red)
                flag = True
            soundObj = pygame.mixer.Sound('drum.mp3')
            soundObj.play()
        for i in range(barN):
            idx = (rectI+i)%barN
            barRect = pygame.Rect(i*(800/barN), 0, (800/barN), 50)
            if bar[idx]==True:
                barSurface.fill(color = (255,255,0),rect=barRect)
            else:
                barSurface.fill(color = (125,125,125), rect =barRect)
        screen.blit(barSurface, (0,0))
    pygame.display.flip()
