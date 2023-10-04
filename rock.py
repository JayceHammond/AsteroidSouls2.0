import pygame as p
from pygame import mixer
import math
import numpy
import random as r


class Rock:
    def __init__(self, color, posx, posy, width, height, screen):
        self.name = "Rock"
        self.color = color
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy
        self.screen = screen

        self.rect = p.Rect(posx, posy, r.randint(30, 60), r.randint(10, 40))
        p.draw.rect(screen, self.color, self.rect)

    def display(self):
        p.draw.rect(self.screen, self.color, self.rect)
