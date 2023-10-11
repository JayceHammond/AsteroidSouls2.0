import os
import pygame as p
from pygame import mixer
import math
import numpy
import random as r
from pathlib import Path

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

file_types = ("png")
file_paths = os.listdir("Assets\AsteroidAssets")

asteroidImgs = []
colorArr = [WHITE, GREEN, RED, ORANGE, YELLOW, CYAN]

class Rock:
    def __init__(self, posx, posy, screen):
        self.name = "Rock"
        self.width = 100
        self.height = 100
        self.posx = posx
        self.posy = posy
        self.screen = screen

        self.rock = p.image.load(file_paths[0])
        self.clean_rock = self.rock.copy()
        #self.rock.set_colorkey(colorArr[r.randint(0, 5)])

    def display(self, screen):
        screen.blit(self.rock, (self.posx - 15, self.posy - 15))

    def update(self):
        self.posy += 1
        i = 0
        while i < len(asteroidImgs):
            self.rock = p.image.load(file_paths[i])

