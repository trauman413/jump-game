# Use this module as a basis for your game. Only run this file when you have downloaded Pygame:
# To download pygame: type this into the command line:
# py -m pip install -U pygame --user



#Imports the pygame module. See https://www.pygame.org/docs/ for details
import pygame
# Other modules
import sys
from pygame.locals import *

lightblue = (0, 128, 255)
orange = (255,100,0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Used to initialize game
pygame.init()

font = pygame.font.SysFont("arial", 72)
font2 = pygame.font.SysFont("arial",48)

text = font.render("Hello, World", True, (0, 255, 0))
text_rect = text.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

subtext = font2.render("what's up",True,(0,0,255))
subtext_rect = text.get_rect(center=(SCREEN_WIDTH/2,400))

# Used to set window caption
pygame.display.set_caption("Game")

# Sets the screen, parameter: tuple with length and width
screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )

# Keeps game running
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()
pygame.key.set_repeat(10,10)
while not done:
        # empties the event queue; necessary to see actions.
        for event in pygame.event.get():
                # Method 1
                # # Checks if a key is down.
                # if event.type == pygame.KEYDOWN:
                #     # checks if the key down is space.
                #     if event.key == pygame.K_SPACE:
                #         is_blue = not is_blue
                # if window is closed

                # Method 2:
                pressed = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if pressed[pygame.K_SPACE]:
                        is_blue = not is_blue
                    if pressed[pygame.K_UP]:
                        y -= 3
                    if pressed[pygame.K_DOWN]:
                        y += 3
                    if pressed[pygame.K_LEFT]:
                        x -= 3
                    if pressed[pygame.K_RIGHT]:
                        x += 3
                if is_blue:
                    color = lightblue
                else:
                    color = orange
                screen.fill( (0,0,0) )
                screen.blit(text,text_rect)
                screen.blit(subtext,subtext_rect)
                if event.type == pygame.QUIT:
                        done = True
                # Draws a rectangle to the screen:
                # Argument 1: draws to the surface assigned
                # Argument 2: RGB tuple
                # Argument 3: rectangle instance. X, Y, width, height
                pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        # Acts as a way to update game screen.
        pygame.display.flip()
        #clock.tick(60)
