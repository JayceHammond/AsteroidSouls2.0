import pygame as p
from pygame import mixer
import math
import numpy
import random as r

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

asteroidImgs = ["Assets\AsteroidAssets\Rock1.png", "Assets\AsteroidAssets\Rock2.png", "Assets\AsteroidAssets\Rock3.png", "Assets\AsteroidAssets\Rock4.png", "Assets\AsteroidAssets\Rock5.png", "Assets\AsteroidAssets\Rock6.png"]
colorArr = [WHITE, GREEN, RED, ORANGE, YELLOW, CYAN]

class Rock:
    def __init__(self, posx, posy, screen):
        self.name = "Rock"
        self.width = 100
        self.height = 100
        self.posx = posx
        self.posy = posy
        self.screen = screen

        self.rock = p.image.load(asteroidImgs[r.randint(0, 5)])
        self.clean_rock = self.rock.copy()
        #self.rock.set_colorkey(colorArr[r.randint(0, 5)])

    def display(self, screen):
        screen.blit(self.rock, (self.posx, self.posy))

    def update(self):
        self.posy += 1
        self.clean_rock = self.rock.copy()
        self.rock = p.transform.rotate(self.clean_rock, 1)
