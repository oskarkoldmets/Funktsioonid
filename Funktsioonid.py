import pygame
import sys
import random 
pygame.init()

#värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)

#funktsioonid
def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((3/4.0) * height)), (x,y), (x+width,y), (x+width,y-(3/4.0) * height), 
        (x,y- ((3/4.0) * height)), (x + width/2.0,y-height), (x+width,y-(3/4.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

#kutsun funktsiooni välja
drawHouse(100,400,300,200,screen, red)
    
pygame.display.flip()
