import pygame

class action():
    def __init__(input_actionType, input_magnitude, input_effect):
        self.actionType = input_actionType #0: attack, 1: heal, 2: buff
        self.magnitude = input_magnitude
        self.effect = input_effect

    def activate(target):
        if self.actionType == 0:
            target.damage(self.magnitude)
            effect.play()
        
