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
dissmessage = ""
dissentTimeOut = 0


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
green = (0, 255, 0)


text = GAME_FONT.render(agreersSTR, True, red, blue)
textRect = text.get_rect()


#ActualThings

def Power2():
    print("Nothing Yet")


def win():
    screen.fill(white)
    winrender = GAME_FONT.render("YOU WIN", True, black)
    screen.blit(winrender, (425, 325))



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
            lastmessagerender = GAME_FONT.render(message, True, green)
            screen.blit(lastmessagerender, (0, 100))
            dissmessagerend = GAME_FONT.render(dissmessage, True, red)
            screen.blit(dissmessagerend, (0, 615))
            agreersSTR = str(agreers)

#Abilities/Propaganda/MakeNumberGoUp

            if keys[pygame.K_a]:
                if pow1timeout == 0:
                    print("Lying to people")
                    message = "Oil is good for you, I drink it everyday"
                    agreers = agreers + 3
                    pow1timeout = 300
            if pow1timeout > 0:
                pow1timeout = pow1timeout - 1
                pow1timeoutstr = str(pow1timeout)
                pow1timeoutrender = GAME_FONT.render(pow1timeoutstr, True, white)
                screen.blit(pow1timeoutrender, (950, 0))
            if keys[pygame.K_s]:
                if pow1timeout == 0:
                    print("Lying to people")
                    message = "Windmills cause cancer"
                    agreers = agreers + 2
                    pow1timeout = 300
            if pow1timeout > 0:
                pow1timeout = pow1timeout - 1
                pow1timeoutstr = str(pow1timeout)
                pow1timeoutrender = GAME_FONT.render(pow1timeoutstr, True, white)
                screen.blit(pow1timeoutrender, (950, 0))




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
            if dissentTimeOut == 0:
                disschance = randint(1, 10)
                if disschance == 3:
                    agreers = agreers - 1
                    distmessagechance = randint (1, 4)
                    dissentTimeOut = 600
                    if distmessagechance == 1:
                        dissmessage = "Oil Drilling Harms Wildlife"
                    if distmessagechance == 2:
                        dissmessage = "Fraking Pollutes the water"
                    if distmessagechance == 3:
                        dissmessage = "Renewables are cheaper for you"
                    if distmessagechance == 4:
                        dissmessage = "Solar Panels are not seasonal"

            if dissentTimeOut > 0:
                dissentTimeOut = dissentTimeOut - 1
            pygame.display.update()
            print(agreers)
            clock.tick(60)