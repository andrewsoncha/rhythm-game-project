import pygame

print('barN')
barN = int(input())
print('barMs')
barMs = int(input())
print('musicPath')
musicPath = input()

beatBarList = [False]*barN
beatBarList[0] = True
pygame.init()
screen = pygame.display.set_mode([800,600])
barSurface = pygame.Surface((800,100))
music = pygame.mixer.Sound(musicPath)

running = True
screenFlag = False
rectI = 0
barPrev = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            beatBarList[rectI] = True
        if event.type == pygame.KEYDOWN:
            running = False
    if pygame.time.get_ticks()-barPrev>barMs:
        #print(rectI)
        barPrev = pygame.time.get_ticks()
        rectI+=1
        rectI%=barN
        if rectI==0:
            music.play()
        flag = beatBarList[rectI]
        if flag:
            screenFlag = not screenFlag
    barRect = pygame.Rect(0, 0, 800, 100)
    barSurface.fill(color = (125,125,125), rect=barRect)
    for i in range(barN):
        barRect = pygame.Rect(800/barN*i, 0, 800/barN, 100)
        if beatBarList[i] == True:
            barSurface.fill(color = (255,255,0),rect=barRect)
        barRect = pygame.Rect(800/barN*rectI, 0, 800/barN, 100)
        barSurface.fill(color = (255,0,0),rect=barRect)
    if screenFlag == True:
        screen.fill((255,255,255))
    else:
        screen.fill((255,0,0))
    screen.blit(barSurface, (0,0))
    pygame.display.update()
    pygame.display.flip()

file = open('beat.txt', 'w')
file.write(str(barN)+'\n')
for i in beatBarList:
    if i:
        file.write('1\n')
    else:
        file.write('0\n')
file.close()
