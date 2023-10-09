import pygame as p
from pygame import mixer
import math
import numpy
import random as r
from collider import Collider

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

class Ship:
    def __init__(self, posx, posy, speed, img, width, height, xDir, yDir, health):
        #Player position and direction values
        self.posx = posx
        self.posy = posy
        self.xDir = xDir
        self.yDir = yDir
        #Image loading
        self.img = img
        #Sizing of ship
        self.width = width
        self.height = height
        #Player Vars
        self.speed = speed
        self.health = health
        self.name = "Player"
        self.ship = p.image.load(self.img)
        self.col = Collider(self)
        #Firing values
        self.firing = False  # Add a flag to track if the gun is firing
        self.fire_cooldown = 15  # Add a cooldown period (in frames) between shots
        self.cooldown_counter = 0  # Initialize the cooldown counter


    def display(self, screen, mousePos):
        self.ship = p.image.load(self.img)
        self.ship = p.transform.rotate(self.ship, -math.degrees(self.getAngle(mousePos)))
        screen.blit(self.ship, (self.posx - 25, self.posy - 25))

    def update(self, xDir, yDir):
            self.posx = self.posx + self.speed * xDir
            self.posy = self.posy + self.speed * yDir

            #self.col.checkCollision(obj, self.xDir, self)


    def getAngle(self, mousePos):
            # Lock the x-coordinate of the mouse at x = 325
            mouse_x = mousePos[0] # Get the x-coordinate of the mouse
            mouse_y = mousePos[1]  # Get the y-coordinate of the mouse

            # Calculate the angle in radians
            angle = math.atan2(mouse_y - self.posy, mouse_x - self.posx)

            # Convert the angle to degrees and ensure it's within -90 to 90 degrees
            angle_degrees = math.degrees(angle)
            adjusted_angle_degrees = angle_degrees if -90 <= angle_degrees <= 90 else (angle_degrees + 180) % 360 - 180

            # Convert the angle back to radians
            adjusted_angle = math.radians(adjusted_angle_degrees)

            return adjusted_angle
    
    def fire(self):
        if not self.firing and self.cooldown_counter <= 0:
            self.firing = True
            self.cooldown_counter = self.fire_cooldown
            return True
        return False

    