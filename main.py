import pygame 
import sys
from pygame.locals import *
import pygame.freetype
from random import randint
import random
import time

pygame.init()
pygame.display.init()
GAME_FONT = pygame.font.Font("Montserrat-Regular.ttf", 24)
numberFont = pygame.font.Font("Tiny5-Regular.ttf", 24)
cooldownFont = pygame.font.Font("Tiny5-Regular.ttf", 16)
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
pow2timeout = 0
dissratemax = 0
pow3timeout = 0
elpasedtime = 1
pow4timeout = 0
pow5timeout = 0
policySelect = False
jailed = 0

pow1messages = ["Oil is good for you, I drink it everyday", "Windmills cause cancer", "Snow disproves Global Warming"]


agreersSTR = str(agreers)

#Images
introScreen = pygame.image.load('intro.png')
diffselectscreen = pygame.image.load('diffselectscreen.png')
background = pygame.image.load('background.png')
policyBackground = pygame.image.load('policybackground.png')


#Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)


#ActualThings
def win():
    screen.fill(white)
    winrender = GAME_FONT.render("YOU WIN, YOU HAVE BOILED THE WORLD", True, black)
    screen.blit(winrender, (425, 325))



def lose():
    screen.fill(white)
    loserender = GAME_FONT.render("YOU LOSE", True, black)
    screen.blit(loserender, (500, 325))


#Policies
def oilContracts():
    global townspeople
    global agreers
    townspeople = townspeople - 1
    agreers = agreers + 1

def teardownWindmills():
    global townspeople
    global agreers
    townspeople = townspeople + 1
    agreers = agreers - 1

def ICanSo():
    global townspeople
    global agreers
    global message
    townspeople = townspeople - 2
    agreers = agreers + 2
    message = "You cant stop me I'm the king"

def RemoveEducation():
    global townspeople
    global agreers
    townspeople = townspeople - 1 
    agreers = agreers + 2


def revolt():
    if agreers >= jailed:
        win()
    if agreers <= jailed:
        lose()




#Main Loop
while running:

    keys = pygame.key.get_pressed()

    #Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





        #Policy 789, 262 -> 860, 335
        if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                #Policy
                if x >= 789:
                    if x <= 860:
                        if y >= 262:
                            if y<= 335:
                                policySelect = True
                # Bribes 916, 262 -> 987, 335
                if x >= 916:
                    if x <= 987:
                        if y >= 262:
                            if y<= 335:
                                if pow5timeout == 0:
                                    print("Bribes")
                                    message = "Money speaks louder than words"
                                    agreers = agreers + 2
                                    townspeople = townspeople - 1
                                    pow5timeout = 300
                # Reuse 789, 110 -> 860, 183
                if x >= 789:
                    if x <= 860:
                        if y >= 110:
                            if y<= 183:
                                if pow1timeout == 0:
                                    print("Lying to people")
                                    message = random.choice(pow1messages)
                                    agreers = agreers + 3
                                    pow1timeout = 300
                # Jail Button 916, 110 -> 987, 183
                if x >= 916:
                    if x <= 987:
                        if y >= 110:
                            if y <= 183:
                                if pow4timeout == 0:
                                    message = "Maybe you will learn your lesson"
                                    agreers = agreers + 2
                                    townspeople = townspeople - 1
                                    pow4timeout = 300
                                    jailed = jailed + 1
                                    print("Jailing")

    #SplashScreen
    if intro <= 500:
        screen.blit(introScreen, (0, 0))
        pygame.display.update()
        intro = intro + 1
        splashscreen = 1
    else:
        splashscreen = 0

    #DiffSelection
    if splashscreen == 0:
        if diffselect == 0:
            screen.blit(diffselectscreen, (0, 0))
            if keys[pygame.K_0]:
                diff = 0
                diffselect = 1
                agreers = 75
                dissrate = 150
                dissratemax = 600
            if keys[pygame.K_1]:
                diff = 1
                diffselect = 1
                agreers = 50
                dissrate = 300
                disratemax = 450
            if keys[pygame.K_2]:
                diff = 2
                diffselect = 1
                agreers = 25
                dissrate = 450
                dissratemax = 300
            if keys[pygame.K_3]:
                diff = 3
                diffselect = 1
                agreers = 15
                dissrate = 500
                dissratemax = 150
            pygame.display.update()

    #Policy
    if diffselect != 0:
        if splashscreen == 0: 
            if policySelect == True:
                screen.blit(policyBackground, (200, 125))
                if keys[pygame.K_p]:
                    policySelect = False
                if keys[pygame.K_q]:
                    oilContracts()
                if keys[pygame.K_w]:
                    teardownWindmills()
                if keys[pygame.K_e]:
                    ICanSo()
                if keys[pygame.K_r]:
                    RemoveEducation()
#                print("Policy Time")
                pygame.display.update()
                clock.tick(60)

    #Main
    if diffselect != 0:
        if splashscreen == 0: 
            if policySelect == False:   #Draw
                screen.blit(background, (0, 0))
                fontrender = numberFont.render(agreersSTR, True, black)
                screen.blit(fontrender, (825, 205))
                townspeoplerender = numberFont.render(str(townspeople), True, black)
                screen.blit(townspeoplerender, (910, 205))
                lastmessagerender = GAME_FONT.render(message, True, black)
                screen.blit(lastmessagerender, (10, 200))
                dissmessagerend = GAME_FONT.render(dissmessage, True, black)
                screen.blit(dissmessagerend, (10, 425))
                agreersSTR = str(agreers)

#Abilities/Propaganda/MakeNumberGoUp

                if keys[pygame.K_a]:
                    if pow1timeout == 0:
                        print("Lying to people")
                        message = random.choice(pow1messages)
                        agreers = agreers + 3
                        pow1timeout = 300
                if pow1timeout > 0:
                    pow1timeout = pow1timeout - 1
                    pow1timeoutstr = str(pow1timeout)
                    pow1timeoutrender = cooldownFont.render(pow1timeoutstr, True, black)
                    screen.blit(pow1timeoutrender, (816, 29))
#                if keys[pygame.K_s]:
#                    if pow2timeout == 0:
#                        print("Lying to people")
#                        message = ""
#                        agreers = agreers + 2
#                        pow2timeout = 300
#                if pow2timeout > 0:
#                    pow2timeout = pow2timeout - 1
#                    pow2timeoutstr = str(pow2timeout)
#                    pow2timeoutrender = GAME_FONT.render(pow2timeoutstr, True, black)
#                    screen.blit(pow2timeoutrender, (950, 20))
#                if keys[pygame.K_d]:
#                    if pow3timeout == 0:
#                        print("Lying to people")
#                        message = ""
#                        agreers = agreers + 2
#                        pow3timeout = 300
#                   if pow3timeout > 0:
#                       pow3timeout = pow3timeout - 1
#                       pow3timeoutstr = str(pow3timeout)
#                       pow3timeoutrender = GAME_FONT.render(pow3timeoutstr, True, black)
#                       screen.blit(pow3timeoutrender, (950, 29))
                if keys[pygame.K_f]:
                    if pow4timeout == 0:
                        print("Jailing people")
                        message = "Maybe you will learn your lesson"
                        agreers = agreers + 2
                        townspeople = townspeople - 1
                        jailed = jailed + 1
                        pow4timeout = 300
                if pow4timeout > 0:
                    pow4timeout = pow4timeout - 1
                    pow4timeoutstr = str(pow4timeout)
                    pow4timeoutrender = cooldownFont.render(pow4timeoutstr, True, black)
                    screen.blit(pow4timeoutrender, (860, 29))
                if keys[pygame.K_o]:
                    policySelect = True
                if keys[pygame.K_g]:
                    if pow5timeout == 0:
                        print("Bribes")
                        message = "Money speaks louder than words"
                        agreers = agreers + 2
                        townspeople = townspeople - 1
                        pow5timeout = 300
                if pow5timeout > 0:
                    pow5timeout = pow5timeout - 1
                    pow5timeoutstr = str(pow5timeout)
                    pow5timeoutrender = cooldownFont.render(pow5timeoutstr, True, black)
                    screen.blit(pow5timeoutrender, (907, 29))




                if dissrate == dissratemax:
                    angerpercent = 1
                    dissrate = 0
                else:
                    angerpercent = 0
                    dissrate = dissrate + 1
                if angerpercent == 1:
                    agreers = agreers - 1
                if agreers <= 0:
                    lose()
                    dissrate = 0
                    if elpasedtime == 3:
                        sys.exit()
                        print("Leaving")
                    else:
                        time.sleep(1)
                        elpasedtime = elpasedtime + 1
                if agreers >= townspeople:
                    win()

#Dissenter Chance
                if dissentTimeOut == 0:
                    disschance = randint(1, 10)
                    if disschance == 3:
                        agreers = agreers - 1
                        distmessagechance = randint (1, 6)
                        dissentTimeOut = 400
                        if distmessagechance == 1:
                            dissmessage = "Oil Drilling Harms Wildlife"
                        if distmessagechance == 2:
                            dissmessage = "Fraking pollutes water"
                        if distmessagechance == 3:
                            dissmessage = "Renewables are cheaper for you"
                        if distmessagechance == 4:
                            dissmessage = "Solar Panels are not seasonal"
                        if distmessagechance == 5:
                            dissmessage = "Oil Refineries spew out toxic gas"
                        if distmessagechance == 6:
                            dissmessage = "Global Warming causes extermes on both ends"

                if dissentTimeOut > 0:
                    dissentTimeOut = dissentTimeOut - 1
#                    print(dissentTimeOut)
                if jailed == 30:
                    revolt()
                
            pygame.display.update()
            #print(agreers)
            clock.tick(60)