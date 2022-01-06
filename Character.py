import math
import pygame
class vec2D:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
    def copy(targetPoint):
        return vec2D(targetVec.x, targetVec.y)
    def __add__(self, other):
        resultX = self.x+other.x
        resultY = self.y+other.y
        return vec2D(resultX, resultY)
    def __sub__(self, other):
        resultX = self.x-other.x
        resultY = self.y-other.y
        return vec2D(resultX, resultY)
    def __mul__(self, other):
        resultX = self.x*other
        resultY = self.y*other
        return vec2D(resultX, resultY)
    def __truediv__(self, other):
        resultX = self.x/other
        resultY = self.y/other
        return vec2D(resultX, resultY)
    def __abs__(self):
        return self.x*self.x+self.y*self.y
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

def normalize(vec):
    return vec/abs(vec)

def distVec(vecA, vecB):
    return abs(vecA-vecB)

def avg(vecA, vecB, alpha = 0.5):
    return (vecA*alpha+vecB*(1-alpha))

def collide(objA, objB):
    if dist(objA, objB)<(objA.radius+objB.radius):
        return True
    else:
        return False

class gameObj(object):#base class for all game objects
    def __init__(self, init_point, init_radius, init_color):#for now all objects are circular. will change into proper sprites later
        self.point = init_point
        self.radius = init_radius
        self.color = init_color
    def draw(self, surface):
        pygame.draw.circle(surface, self.color,(self.point.x, self.point.y), self.radius)


def dist(objA, objB):
       return math.sqrt(distVec(objA.point, objB.point))

    
class character(gameObj):#base class for all characters
    def __init__(self, init_point, init_radius, init_color, init_speed, init_health, init_attack, init_attackType = 0):
        print(init_point)
        super().__init__(init_point, init_radius, init_color)
        self.target = None
        self.speed = init_speed
        self.health = init_health
        self.maxHealth = init_health
        self.attack = init_attack
        self.attackType = init_attackType
    def updateTarget(self, characterList):
        sortedList = sorted(characterList, key=lambda char:dist(char, self))
        self.target = sortedList[0]
    def moveTowardTarget(self):
        if self.target != None:
            #if not already collided, go toward target
            if not collide(self, self.target):
                direction = self.target.point-self.point
                direction = normalize(direction)
                direction *= self.speed
                self.point += direction
    def characterAttack(self):
        if self.attackType==1:
            self.target.health-=self.attack
            if self.target.health<0:
                self.target.health = 0
            direction = self.target.point-self.point
            self.target.point += normalize(direction)*1000.0
            soundObj = pygame.mixer.Sound('clubHit.mp3')
            soundObj.play()
    def update(self, surface, characterList, attackAvailable):
        #this function is called every frame the character exists
        #make up target->move toward target->if it is time to attack, attack
        if len(characterList)>0:
            self.updateTarget(characterList)
            self.moveTowardTarget()
            if attackAvailable and collide(self, self.target) and self.target.health>0:
                self.characterAttack()
        self.draw(surface)
        #todo: check if it's the right time to attack and attack
    def draw(self, surface):
        #this function will probably get overloaded in the playerCharacter and the enemy class
        #todo: change the class to have the characters have its own color/sprite and draw it accordingly
        #super().draw(surface)
        gray = (125,125,125)
        drawColor = (self.color[0]*(self.health/self.maxHealth)+125*(1-self.health/self.maxHealth),self.color[1]*(self.health/self.maxHealth)+125*(1-self.health/self.maxHealth),self.color[2]*(self.health/self.maxHealth)+125*(1-self.health/self.maxHealth))
        pygame.draw.circle(surface, drawColor,(self.point.x, self.point.y), self.radius)
