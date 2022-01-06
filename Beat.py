import pygame

class timer:
    def __init__(self, init_beatMs):
        self.beatMs = init_beatMs
        self.beats = []
        self.beatBarIdx = []
    def attach(self, beatObj):
        self.beats.append(beatObj)
        self.beatBarIdx.append(0)
    def moveOneBar(self):
        currentBeatStatus = []
        for beatI in self.beats:
            currentBeatStatus.append(beatI.beatBars[beatBarIdx])
            beatBarIdx+=1
            beatBarIdx%=beatI.beatN
        return currentbeatStatus

class beat:
    def __init__(self, init_timer, init_beatBars, init_beatN=200, init_soundObj=None):
        self.timer = init_timer
        self.beatBars = init_beatBars
        self.beatN = init_beatN
        self.soundObj = init_soundObj
        self.timer.attach(self)
    
    def makeFromBpm(init_timer, beatN, bpm, soundObj):
        bar = [False]*beatN
        
        for i in range(barN):
            if barMs*i%int(60000/bpm)==0:
               bar[i] = True

        return beat(init_timer, bar,200, 4000, pygame.mixer.Sound('drum.mp3'))
