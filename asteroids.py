import pygame as p
from pygame import mixer
import math
import numpy
import random as r
from ship import Ship
from rock import Rock
from healthbar import HealthBar
from bullet import Bullet
from button import Button

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREY = (128,128,128)

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
asteroidArray = []

#GAME VARS
playerSpeed = 7

#INITIALIZE GAME
def gameInit():
    #GLOBAL VARS
    global screen
    global surface
    global player
    global healthBar
    p.init()
    if state == "GAME":
        p.mouse.set_visible(False)
    else:
        p.mouse.set_visible(True)
    mixer.init()
    screen = p.display.set_mode(size, p.RESIZABLE) 
    p.display.set_caption(title)
    surface = p.Surface(size)
    #objArray.append(rock)
    player = Ship(screenWidth / 2, screenHeight / 2, playerSpeed, playerSprite, 10, 20, 0, 0, 100)
    healthBar = HealthBar(0, 675, player.health)
    

def displayTitle():
        font = p.font.Font("Assets\Evil Empire.otf", 100)
        text = font.render("Asteroid", True, ORANGE, BLACK)
        text2 = font.render("Souls", True, ORANGE, BLACK)
        textRect = text.get_rect()
        text2Rect = text.get_rect()
        textRect.center = (350,150)
        text2Rect.center = (420, 250)
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)


#DISPLAY GAME
def gameDisplay():
    if state == "GAME":
        screen.fill(BLACK)
        drawMouse()
        player.display(screen, mousePos)
        healthBar.displayHealth(screen)
        displayObjArray()
        displayKills(killCount, 600, 675)
        for rock in asteroidArray:
            rock.display(screen)
        p.display.update()
        clock.tick(60)

    if state == "START":
        screen.fill(BLACK)
        global startButton
        startButton = Button("Start", 350, 350)
        optionsButton = Button("Options", 350, 400)
        displayTitle()
        startButton.display(screen)
        optionsButton.display(screen)
        p.display.update()
        clock.tick(60)
        return startButton
        

def randomizeRockSpawn():
    rockSpawnZone = (r.randint(0, 700), r.randint(0, 100))
    return rockSpawnZone

def drawMouse():
    crosshair = p.image.load("Assets\crosshair.png")
    crosshairRect = crosshair.get_rect()
    crosshairRect.center = (mousePos)
    screen.blit(crosshair, crosshairRect)

def displayKills(count, x , y):
    font = p.font.Font("Assets\Evil Empire.otf", 40)
    text = font.render("Kills: " + str(count), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (x, y)

    screen.blit(text, textRect)

def displayObjArray():
    if objArray:
        for bullet in objArray:
            bullet.display(screen)
            bullet.update()

def spawnRock(spawnNum):
    i = 0
    while i < spawnNum:
        rock = Rock(randomizeRockSpawn()[0], randomizeRockSpawn()[1], screen)
        asteroidArray.append(rock)
        i += 1


def main():
    global killCount
    global state
    xDir, yDir = 0, 0
    running = True
    killCount = 0
    #STATE
    state = "START"
    spawnable = True
    gameInit()
    spawnRock(5)
    while running:
        global mousePos
        mousePos = p.mouse.get_pos()
        if state == "START":
            for event in p.event.get():
                if event.type == p.QUIT:
                    return
                if event.type == p.MOUSEBUTTONDOWN:
                    if(mousePos[0] >= startButton.x - 45 and mousePos[0] <= 400):
                        state = "GAME"

            gameDisplay()
            
        if state == "GAME":
            angle = player.getAngle(mousePos)
            if len(asteroidArray) == 0:
                spawnRock(5)
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
                    shot = Bullet(player.posx, player.posy, RED, 5, 10, angle)
                    objArray.append(shot)

                for bullet in objArray:
                    for rock in asteroidArray:
                        if bullet.check_collision(rock):
                            killCount += 1
                            asteroidArray.remove(rock)
                            if objArray: 
                                objArray.remove(bullet)
                

            

    #UPDATE
            player.update(xDir, yDir)
            for rock in asteroidArray:
                rock.update()
            if healthBar.updateHealth(player.col.checkCollision(asteroidArray, xDir, player)):
                main()
    #DISPLAY
            gameDisplay()


main()