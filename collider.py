import pygame as p
from pygame import mixer
import math
import numpy
import random as r

class Collider:
    def __init__(self, parent):
        self.posx = parent.posx
        self.posy = parent.posy
        self.width = parent.width
        self.height = parent.height
        self.center = (self.posx, self.posy)
    
    def checkCollision(self, obj, xDir):
        #Calculate the distance between the collider and the center of the obj
        distance = math.sqrt((self.posx - obj.posx) ** 2 + (self.posy - obj.posy) ** 2)

        #Check if a collision has occurred
        if distance < (self.width / 2) + (obj.width / 2):
            self.posx += (obj.width / 2) * (-xDir)
            print("COLLIDED")