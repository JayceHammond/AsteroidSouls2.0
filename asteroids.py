import pygame as p
from pygame import mixer
import math
import numpy
import random as r
from ship import Ship
from rock import Rock
from healthbar import HealthBar
from bullet import Bullet

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
rockSpawnZone = (r.randint(0, 700), r.randint(0, 100))

#GAME VARS
playerSpeed = 7

#INITIALIZE GAME
def gameInit():
    #GLOBAL VARS
    global screen
    global surface
    global player
    global rock
    global healthBar
    p.init()
    p.mouse.set_visible(False)
    mixer.init()
    screen = p.display.set_mode(size, p.RESIZABLE) 
    p.display.set_caption(title)
    surface = p.Surface(size)
    rock = Rock(rockSpawnZone[0], rockSpawnZone[1], screen)
    #objArray.append(rock)
    player = Ship(screenWidth / 2, screenHeight / 2, playerSpeed, playerSprite, 10, 20, 0, 0, 100)
    healthBar = HealthBar(0, 675, player.health)
    

#DISPLAY GAME
def gameDisplay():
    screen.fill(BLACK)
    drawMouse()
    player.display(screen, mousePos)
    healthBar.displayHealth(screen)
    displayObjArray()
    rock.display(screen)
    p.display.update()
    clock.tick(60)

def drawMouse():
    crosshair = p.image.load("Assets\crosshair.png")
    crosshairRect = crosshair.get_rect()
    crosshairRect.center = (mousePos)
    screen.blit(crosshair, crosshairRect)

def displayObjArray():
    if objArray:
        for bullet in objArray:
            bullet.display(screen)
            bullet.update()


def main():
    gameInit()
    xDir, yDir = 0, 0
    running = True
    while running:
        global mousePos
        mousePos = p.mouse.get_pos()
        angle = player.getAngle(mousePos)
        for event in p.event.get():
            p.event.set_grab(False)
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
            if event.type == p.MOUSEBUTTONDOWN:
                shot = Bullet(player.posx, player.posy, RED, 5, 10, angle,)
                objArray.append(shot)

        

#UPDATE
        player.update(xDir, yDir, rock)
        rock.update()
        if healthBar.updateHealth(player.col.checkCollision(rock, xDir, player)):
            main()
#DISPLAY
        gameDisplay()


main()