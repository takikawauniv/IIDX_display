import pygame
from pygame.locals import *
import sys
import time


SCREEN_WIDTH = 350
SCREEN_HEIGHT = 200
SPEED = 1.0

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


class JoyStatus:
    def __init__(self):
        self.btn = [0,0,0,0,0,0,0,0,0,0,0,0]

JStat = JoyStatus()

class Position:
    def __init__(self):
        self.clear()
    def clear(self):
        self.x = 0.0
        self.y = 0.0
        
Pos = Position()
pygame.joystick.init()
try:
    joy = pygame.joystick.Joystick(0)

except pygame.error:
    print("error!")
    sys.exit()

_scratch = pygame.image.load("cinnamon.png")
scratch = pygame.transform.smoothscale(_scratch,(100,100))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('IIDX controller')
    pygame.display.flip()
    
    
    while True:
        #event
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        
        # Stick
        JStat.axLx = joy.get_axis(0)

        for i in range(12):
            if joy.get_button(i) == 1:
                JStat.btn[i] = 0
            else:
                JStat.btn[i] = 1

        ShowPad(screen)

        pygame.time.wait(10)

    return

def ShowPad(screen):
    font = pygame.font.Font(None, 18)

    Pos.x = 110
    Pos.y = 110  
    screen.fill((0,0,0))
    rotated_scr = rot_center(scratch,JStat.axLx * 180)


    pygame.draw.rect(screen, (255,255,255), Rect(180,120,33,49), JStat.btn[0])    #1
    pygame.draw.rect(screen, (255,255,255), Rect(200,65,33,49), JStat.btn[1])     #2
    pygame.draw.rect(screen, (255,255,255), Rect(220,120,33,49), JStat.btn[2])    #3
    pygame.draw.rect(screen, (255,255,255), Rect(240,65,33,49), JStat.btn[3])     #4
    pygame.draw.rect(screen, (255,255,255), Rect(260,120,33,49), JStat.btn[4])    #5
    pygame.draw.rect(screen, (255,255,255), Rect(280,65,33,49), JStat.btn[5])     #6
    pygame.draw.rect(screen, (255,255,255), Rect(300,120,33,49), JStat.btn[6])    #7
    pygame.draw.rect(screen, (255,255,255), Rect(180,20,33,33), JStat.btn[8])     #one
    pygame.draw.rect(screen, (255,255,255), Rect(220,20,33,33), JStat.btn[9])     #two
    pygame.draw.rect(screen, (255,255,255), Rect(260,20,33,33), JStat.btn[10])    #three
    pygame.draw.rect(screen, (255,255,255), Rect(300,20,33,33), JStat.btn[11])    #four

    screen.blit(rotated_scr, (60,65)) #scratch
    text = font.render("rotate: {:.3f}".format(JStat.axLx), True, (255,255,255))
    screen.blit(text, [10,180])
    pygame.display.update()


if __name__ == '__main__':
    main()