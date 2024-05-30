'''This program is focused on :
detect collision between two objects by detecting their distance, python math module will be introduced 
Add text in the screen 
''' 
import pygame                                                                         #Day 13 
import random 
import math 

# Initializing pygame 
pygame.init() 

gameStatus = True 
#//q. What code we would write for setting up the screen? 
# Create screen 
screen = pygame.display.set_mode((800, 600)) 

# Set caption in the window 
pygame.display.set_caption('Lesson 8 : collision detection carrot chase game') 

# Change the icon on the top 
icon = pygame.image.load('bear.png') 
pygame.display.set_icon(icon) 

'''Setting up background image''' 
backImage = pygame.image.load('lesson7_nature.png') 

'''image rabbit''' 
rabbit = pygame.image.load('rabbit.png') 
rabbitx = 400 
rabbity = 300 
rabbitxChange = 0 
rabbityChange = 0 

'''image carrot''' 
# There will be multiple carrots placed all over the screen 
carrot = [] 
carrotx = [] 
carroty = [] 
noOfCarrot = 15 
# putting the attributes inside a carrot 
for i in range(noOfCarrot):   
    #//q. How many times will the for loop work? 
    carrot.append(pygame.image.load('carrot.png')) 
    carrotx.append(random.randint(64, 736)) 
    carroty.append(random.randint(0, 510)) 

'''image fox'''                                                                       #day 14 
# There will be multiple carrots placed all over the screen 
fox = [] 
foxx = [] 
foxy = [] 
foxXChange = [] 
foxYChange = [] 
noOfFox = 6 
# putting the attributes inside a fox 
for i in range(noOfFox): 
    fox.append(pygame.image.load('fox.png')) 
    foxx.append(random.randint(64, 736)) 
    foxy.append(random.randint(0, 510)) 
    foxXChange.append(1) 
    foxYChange.append(40) 

'''Add text in the screen to show score''' 
score = 0 
scoreVal = pygame.font.Font('freesansbold.ttf', 32) 
fontx = 10 
fonty = 10 

collisionVal = pygame.font.Font('freesansbold.ttf', 32) 
collx = 600 
colly = 10 

# game over font 
over = pygame.font.Font('freesansbold.ttf', 70) 
gameOverx = 200 
gameOvery = 250 

def showScore(): 
    scoreRender = scoreVal.render('Score : ' + str(score), True, (255, 255, 255)) 
    screen.blit(scoreRender, (fontx, fonty)) 

    collRender = collisionVal.render('Collision : ' + str(collisionCount), True, (255, 255, 255)) 
    screen.blit(collRender, (collx, colly)) 


def placeRabbit(x, y): 
    screen.blit(rabbit, (x, y)) 


def placeCarrot(i): 
    screen.blit(carrot[i], (carrotx[i], carroty[i])) 


def placeFox(i):                                                                         #day 15 
    screen.blit(fox[i], (foxx[i], foxy[i])) 


# implying collision algorithm to detect collision 
def isCollision(x1, y1, x2, y2): 
    # print('checking collision ' +str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2)) 
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)) 
#//q. Which package allows you to get the above functions? 
    # print('distance : '+str(distance)) 
    if distance <= 27: 
        # print('collision') 
        return True 
    return False 

def showGameOver(x, y): 
    gameOver = over.render("GAME OVER", True, (255, 255, 255)) 
    screen.blit(gameOver, (x, y)) 

#parameter to detect collision between a rabbit and a fox 
collisionCount = 0 
# While loop to get events and make the window stay 
running = True 
while running: 
    # print('pygame running') 
    # Change background color 
    # screen.fill((255, 0, 0)) 
    '''Setting up background image''' 
    screen.blit(backImage, (0, 0)) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT: 
                rabbitxChange = 2 
            if event.key == pygame.K_LEFT: 
                rabbitxChange = -2 
            if event.key == pygame.K_UP: 
                rabbityChange = -2 
            if event.key == pygame.K_DOWN: 
                rabbityChange = 2 
        if event.type == pygame.KEYUP: 
            rabbitxChange = 0 
            rabbityChange = 0 

    # Drawing figures 
    rabbitx += rabbitxChange 
    rabbity += rabbityChange 


    # iterating through carrots to detect collision                        #day 16 
    for i in range(noOfCarrot): 
        # print('in i') 
        if isCollision(carrotx[i], carroty[i], rabbitx, rabbity): 
            carrotx[i] = random.randint(64, 736) 
            carroty[i] = random.randint(0, 510) 
            if gameStatus: 
             score += 1 
            print(score) 

        # print('carrot : '+str(i)) 
        placeCarrot(i) 
    for i in range(noOfFox): 
        foxx[i] += foxXChange[i] 
        if foxx[i] <= 0: 
            foxXChange[i] = 1 
            foxy[i] += foxYChange[i] 
        elif foxx[i] >= 736: 
            foxXChange[i] = -1 
            foxy[i] += foxYChange[i] 
        if foxy[i] > 536: 
            foxx[i] = random.randint(64, 736) 
            foxy[i] = random.randint(0, 510) 
        if isCollision(foxx[i],foxy[i], rabbitx, rabbity) : 
            foxx[i] = random.randint(64, 736) 
            foxy[i] = random.randint(0, 510) 

            if gameStatus: 
                collisionCount += 1 
                score -= 1 
        if collisionCount >= 6: 
            print('game over') 
            score = 0 
            gameStatus = False 
            showGameOver(gameOverx, gameOvery) 


        placeFox(i) 

    if rabbitx > 736: 
        rabbitx = 736 
    elif rabbitx <= 0: 
        rabbitx = 0 

    if rabbity > 510: 
        rabbity = 510 
    elif rabbity <= 0: 
        rabbity = 0 
    # call function to draw the image 
    placeRabbit(rabbitx, rabbity) 
    showScore() 

    # Updating the display of pygame, need to do this after any change in the screen 
    pygame.display.update() 