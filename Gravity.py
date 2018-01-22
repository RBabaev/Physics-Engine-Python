#Robert Babaev
#Gravity
#Version 1.0

import pygame, sys, math
from pygame.locals import *

pygame.init()
FPS = 30 
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption('GRAVITYTEST')
BLUE = [10,10,255]
WHITE = [255, 255, 255]
x = int(500)
y = int(50)
radius = 20
speed = 10
friction = 1
mass = 50
groundMass = 1000
testOBJ1 = pygame.draw.circle(DISPLAYSURF, BLUE, (x, y), radius, 0)

while True:
    DISPLAYSURF.fill(BLUE)
    if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
        if x != 1000 - radius:
            x += speed
            friction = 1
        else:
            friction = 2
    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        if x!= 0 + radius:
            x -= speed
        else:
            friction = 2
            friction = 1
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    force = 10 * ((mass * groundMass)/((700 - y)) ** 2)
    if y < 700 - radius:
        y += int(force / friction)
    else:
        y = 700- radius

    testOBJ1 = pygame.draw.circle(DISPLAYSURF, WHITE, (x, y), radius, 0)
    
    pygame.display.update()
    fpsClock.tick()
