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
    
    def makeFromBpm(init_timer, beatN, bpm, soundObj):
        bar = [False]*beatN
        
        for i in range(beatN):
            if init_timer.beatMs*i%int(60000/bpm)==0:
               bar[i] = True

        return beat(init_timer, bar,200, pygame.mixer.Sound('drum.mp3'))
