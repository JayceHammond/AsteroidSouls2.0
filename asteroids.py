import pygame as p
from pygame import mixer
import math
import numpy
import random as r
from ship import Ship
from rock import Rock

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#DISPLAY CONSTS
screenWidth = 700
screenHeight = 700
size = (screenWidth, screenHeight)

#PATHS
    #SPRITES
playerSprite = "Assets\spaceship.png"

#UI CONSTS
title = "Asteroid Souls"

#GAME CONSTS
clock = p.time.Clock()
objArray = []

#GAME VARS
playerSpeed = 7

#INITIALIZE GAME
def gameInit():
    #GLOBAL VARS
    global screen
    global surface
    global player
    global rock
    p.init()
    
    p.mouse.set_visible(False)
    mixer.init()
    screen = p.display.set_mode(size, p.RESIZABLE) 
    p.display.set_caption(title)
    surface = p.Surface(size)
    rock = Rock(RED, r.randint(0, 700), 10, 30, 20, screen)
    objArray.append(rock)
    player = Ship(screenWidth / 2, screenHeight / 2, playerSpeed, playerSprite, 10, 20, 0, 0)
    

#DISPLAY GAME
def gameDisplay():
    screen.fill(BLACK)
    drawMouse()
    player.display(screen, mousePos)
    rock.display()
    p.display.update()
    clock.tick(60)

def drawMouse():
    crosshair = p.image.load("Assets\crosshair.png")
    crosshairRect = crosshair.get_rect()
    crosshairRect.center = (mousePos)
    screen.blit(crosshair, crosshairRect)


def main():
    gameInit()
    xDir, yDir = 0, 0
    running = True
    while running:
        global mousePos
        mousePos = p.mouse.get_pos()
        angle = player.getAngle(mousePos)
        for event in p.event.get():
            p.event.set_grab(True)
            if event.type == p.QUIT:
                return
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    return
                #CONTROLS
                if event.key == p.K_w:
                    yDir = -1
                if event.key == p.K_s:
                    yDir = 1
                if event.key == p.K_d:
                    xDir = 1
                if event.key == p.K_a:
                    xDir = -1
            if event.type == p.KEYUP:
                if event.key == p.K_w or event.key == p.K_s:
                    yDir = 0
                if event.key == p.K_d or event.key == p.K_a:
                    xDir = 0

#UPDATE
        player.update(xDir, yDir, rock)
        
#DISPLAY
        gameDisplay()


main()