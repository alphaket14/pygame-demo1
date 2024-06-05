'''This program is focused on how to do basic operation using pygame - 
create screen, 
set caption, 
change background colour, 
draw shapes, 
setting up basic key press events ie: changing colour of the figure on key press''' 
import pygame 

#Initializing pygame 
pygame.init() 

#Create screen 
screen = pygame.display.set_mode((400,400)) 

#Set caption in the window 
pygame.display.set_caption('Lesson 7 : make figures using pygame') 

#Change the icon on the top 
icon = pygame.image.load('bear.png') 
pygame.display.set_icon(icon) 

#setting up colour for rectangle, to change it with key press 
rectColour = (255, 255, 255) 

running = True 

#While loop to get events and make the window stay 
while running: 
    print('pygame running') 
    # Change background color 
    screen.fill((255, 0, 0)) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_0: 
                rectColour = (0, 255, 0) 
        if event.type == pygame.KEYUP: 
                rectColour = (255, 255, 255) 
        '''
        Checks for Pygame events. If the window is closed, it sets running to False to exit the loop. 
        If the '0' key is pressed(Key-down), it changes the rectangle color to green. If any key is released(Key-UP), 
        it changes the rectangle color back to white.
        '''

    #Drawing figures 
    pygame.draw.rect(screen, rectColour, pygame.Rect(20, 20, 100, 100)) 
    pygame.draw.circle(screen,(255,255,255),(200,200),50) 
    pygame.draw.line(screen,(255,255,255), (100,100),(200,200),10) 
    #Updating the display of pygame, need to do this after any change in the screen 
    pygame.display.update() 
















#Code 2: 
'''This program is focused on : 
Move the shapes on key press - right, left, up, down 
Restrict the shape to move within the screen 
''' 
import pygame 
# Initializing pygame 
pygame.init() 
# Create screen 
screen = pygame.display.set_mode((400, 400)) 
# Set caption in the window 
pygame.display.set_caption('Lesson 7 : make figures using pygame') 
# Change the icon on the top 
icon = pygame.image.load('bear.png') 
pygame.display.set_icon(icon) 
'''setting up colour for rectangle, to change it with key press''' 
rectColour = (255, 255, 255) 
rectX1 = 200 
rectY1 = 200 
rectX2 = 50 
rectY2 = 50 
rectXChange = 0 
rectYChange = 0 

# While loop to get events and make the window stay 
running = True 
while running: 
    print('pygame running') 
    # Change background color 
    screen.fill((255, 0, 0)) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT: 
                rectXChange = .3 
            if event.key == pygame.K_LEFT: 
                rectXChange = -.3 
            if event.key == pygame.K_UP: 
                rectYChange = -.3 
            if event.key == pygame.K_DOWN: 
                rectYChange = .3 
        if event.type == pygame.KEYUP: 
            rectXChange = 0 
            rectYChange = 0 

    '''
    If the right, left, up, or down key is pressed, it changes the rectangle's position accordingly. 
    If any key is released, it stops changing the rectangle's position.

    If the left arrow key is pressed, rectXChange = -.3 sets the variable rectXChange to -.3. 
    This value could be used to change the position of an object (like a rectangle) on the screen. 
    The negative value suggests that the object would move to the left on the 
    x-axis (as the screen's origin (0,0) is at the top left corner). 
    The .3 is likely a speed factor, determining how fast or how many pixels the object moves 
    per frame or event loop iteration.
    '''
    # Drawing figures 
    rectX1 += rectXChange 
    rectY1 += rectYChange 
    if rectX1 > 350 : 
        rectX1 = 350 
    elif rectX1 <= 0: 
        rectX1 = 0 

    if rectY1 > 350 : 
        rectY1 = 350 
    elif rectY1 <= 0: 
        rectY1 = 0 
    pygame.draw.rect(screen, rectColour, pygame.Rect(rectX1, rectY1, rectX2, rectY2)) 

    # Updating the display of pygame, need to do this after any change in the screen 
    pygame.display.update() 



#code 3:
'''
This program will create a screen with a moving rectangle that changes color when it hits 
the screen edges. It also includes a circle that follows the mouse cursor.
'''
import pygame
import random

# Initializing pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((400, 400))

# Set caption in the window
pygame.display.set_caption('Lesson 8 : Advanced operations using pygame')

# Change the icon on the top
icon = pygame.image.load('bear.png')
pygame.display.set_icon(icon)

# Setting up colour for rectangle, to change it with key press
rectColour = (255, 255, 255)
rectX1 = 200
rectY1 = 200
rectX2 = 50
rectY2 = 50
rectXChange = 0.3
rectYChange = 0.3

# Setting up colour for circle
circleColour = (0, 0, 255)

# While loop to get events and make the window stay
running = True
while running:
    print('pygame running')
    # Change background color
    screen.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Check if mouse is inside the rectangle
            if rectX1 < mouse_pos[0] < rectX1 + rectX2 and rectY1 < mouse_pos[1] < rectY1 + rectY2:
                # Change rectangle color
                rectColour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Drawing figures
    rectX1 += rectXChange
    rectY1 += rectYChange

    # If rectangle hits the edge, change direction
    if rectX1 > 350 or rectX1 < 0:
        rectXChange = -rectXChange
    if rectY1 > 350 or rectY1 < 0:
        rectYChange = -rectYChange

    pygame.draw.rect(screen, rectColour, pygame.Rect(rectX1, rectY1, rectX2, rectY2))

    # Draw a circle at the mouse position
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, circleColour, mouse_pos, 20)

    # Updating the display of pygame, need to do this after any change in the screen
    pygame.display.update()

    '''
    This code introduces the following new concepts:
    Random color generation with the random module.
    Collision detection with the screen edges.
    Mouse position tracking with pygame.mouse.get_pos().
    modify the code to change the rectangle's color when it's clicked by the mouse.
    '''