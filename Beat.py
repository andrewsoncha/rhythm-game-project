import pygame

class timer:
    def __init__(self, init_beatMs):
        self.beatMs = init_beatMs
        self.beats = []
        self.beatBarIdx = []
        self.beatN = 0
    def attach(self, beatObj):
        self.beats.append(beatObj)
        self.beatBarIdx.append(0)
        self.beatN+=1
    def moveOneBar(self):
        currentBeatStatus = []
        for i in range(self.beatN):
            currentBeatStatus.append(self.beats[i].beatBars[self.beatBarIdx[i]])
            self.beatBarIdx[i]+=1
            self.beatBarIdx[i]%=self.beats[i].beatN
        return currentBeatStatus

class beat:
    def __init__(self, init_timer, init_beatBars, init_beatN, init_soundObj):
        self.timer = init_timer
        self.beatBars = init_beatBars
        self.beatN = init_beatN
        self.soundObj = init_soundObj
        self.timer.attach(self)

    def load(init_timer, init_soundObj, file_path):
        file = open(file_path, 'r')
        barN = int(file.readline())
        barList = [False]*barN
        for i in range(barN):
            line = file.readline()
            if int(line)==0:
                barList[i] = False
            else:
                barList[i] = True
        file.close()
        return beat(init_timer, barList, barN, init_soundObj)
    
    def makeFromBpm(init_timer, beatN, bpm, init_soundObj):
        bar = [False]*beatN
        
        for i in range(beatN):
            if init_timer.beatMs*i%int(60000/bpm)<init_timer.beatMs:
               bar[i] = True
        if init_soundObj==None:
            soundObj = pygame.mixer.Sound('drum.mp3')
        else:
            soundObj = init_soundObj
        return beat(init_timer, bar,beatN, soundObj)
