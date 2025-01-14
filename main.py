import pygame 
import sys
from pygame.locals import *
import pygame.freetype
from random import randint

pygame.init()
pygame.display.init()
GAME_FONT = pygame.font.Font("Montserrat-Regular.ttf", 24)
running = True

#BASIC
pygame.display.set_caption('Earth Science Final Project')
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((1000, 650))
intro = 0
agreers = 0
diffselect = 0
diff = 0

agreersSTR = str(agreers)

#Images
introScreen = pygame.image.load('intro.png')
diffselectscreen = pygame.image.load('diffselectscreen.png')


#Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
backgroundcolor = (40, 40, 40)


text = GAME_FONT.render(agreersSTR, True, red, blue)
textRect = text.get_rect()

#Main Loop
while running:

    keys = pygame.key.get_pressed()


    
    #Quit
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    #SplashScreen
    if intro <= 500:
        screen.blit(introScreen, (0, 0))
        pygame.display.update()
        intro = intro + 1
        splashscreen = 1
    else:
        splashscreen = 0

    if splashscreen == 0:
        if diffselect == 0:
            screen.blit(diffselectscreen, (0, 0))
            if keys[pygame.K_0]:
                diff = 0
                diffselect = 1
                agreers = 75
            if keys[pygame.K_1]:
                diff = 1
                diffselect = 1
                agreers = 50
            if keys[pygame.K_2]:
                diff = 2
                diffselect = 1
                agreers = 25
            if keys[pygame.K_3]:
                diff = 3
                diffselect = 1
                agreers = 0
            pygame.display.update()

    if diffselect != 0:
        if splashscreen == 0:    #Draw
            screen.fill(backgroundcolor)
            fontrender = GAME_FONT.render(agreersSTR, True, white)
            screen.blit(fontrender, (0, 0))
            agreersSTR = str(agreers)
            pygame.display.update()
            print(agreers)
            clock.tick(60)