import pygame
import sys
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Used to initialize game
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("overthere.mp3")
pygame.mixer.music.play(-1,0.0)


# Used to set window caption
pygame.display.set_caption("Jump Game")

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        #self.rect.left, self.rect.top = location

sky = Background("sky.jpg")


def main():
    # Sets the screen, parameter: tuple with length and width
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    screen.fill((255,255,255))
    start = True
    done = False
    while not done:
        # empties the event queue; necessary to see actions.
        for event in pygame.event.get():
                # if window is closed
                if start:
                        font = pygame.font.SysFont("arial", 72)
                        font2 = pygame.font.SysFont("arial",48)
                        font3 = pygame.font.SysFont("arial",48)

                        text = font.render("Jumpy Game", True, (0, 255, 0))
                        text_rect = text.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/3))

                        subtext = font2.render("Play Now",True,(0,0,255))
                        subtext_rect = text.get_rect(center=(470,350))

                        subtext2 = font2.render("Controls",True,(0,0,255))
                        subtext_rect2 = text.get_rect(center=(470,450))

                        screen.blit(text,text_rect)
                        screen.blit(subtext,subtext_rect)
                        screen.blit(subtext2,subtext_rect2)

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            if subtext_rect.collidepoint(pos):
                                start = False
                else:
                    newscreen(screen)
                pressed = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if pressed[pygame.K_x]:
                        done = True
                if event.type == pygame.QUIT:
                        done = True
        # Acts as a way to update game screen.
        pygame.display.flip()

def newscreen(screen):
    screen.fill((0,0,0))
    screen.blit(sky.image,sky.rect)



if __name__ == "__main__":
    main()
