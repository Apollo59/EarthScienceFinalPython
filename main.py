import pygame 
import sys
from pygame.locals import *
import pygame.freetype
from random import randint
import time

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
dissrate = 0
angerpercent = 0
townspeople = 100
pow1timeout = 0
message = ""


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


#ActualThings

def Power2():
    print("Nothing Yet")




def lose():
    screen.fill(white)
    loserender = GAME_FONT.render("YOU LOSE", True, black)
    screen.blit(loserender, (500, 325))




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
                dissrate = 150
            if keys[pygame.K_1]:
                diff = 1
                diffselect = 1
                agreers = 50
                dissrate = 300
            if keys[pygame.K_2]:
                diff = 2
                diffselect = 1
                agreers = 25
                dissrate = 450
            if keys[pygame.K_3]:
                diff = 3
                diffselect = 1
                agreers = 0
                dissrate = 500
            pygame.display.update()

    if diffselect != 0:
        if splashscreen == 0:    #Draw
            screen.fill(backgroundcolor)
            fontrender = GAME_FONT.render(agreersSTR + "/100", True, white)
            screen.blit(fontrender, (0, 0))
            lastmessagerender = GAME_FONT.render(message, True, white)
            screen.blit(lastmessagerender, (0, 100))
            agreersSTR = str(agreers)
            if keys[pygame.K_a]:
                if pow1timeout == 0:
                    print("Lying to people")
                    message = "Oil is good for you."
                    agreers = agreers + 3
                    pow1timeout = 300
            if pow1timeout > 0:
                pow1timeout = pow1timeout - 1
            if dissrate == 600:
                angerpercent = 1
                dissrate = 0
            else:
                angerpercent = 0
                dissrate = dissrate + 1
            if angerpercent == 1:
                agreers = agreers - 1
            if agreers == 0:
                lose()
                dissrate = 0

#Dissenter Chance


            pygame.display.update()
            print(agreers)
            clock.tick(60)