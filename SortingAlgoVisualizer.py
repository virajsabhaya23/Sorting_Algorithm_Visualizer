import random
import pygame
pygame.init()

class DrawInfo:
    BLACK = 0,0,0
    WHITE = 255,255,255
    RED =  255,0,0
    GREEN = 0,255,0
    BLUE = 0,0,255
    GREY = 128,128,128
    BG = 24,24,24
    BACKGROUND_COLOR = BG

    def __init__(self,width,height,lst):
        self.width = width
        self.height = height
        
        self.widnow = pygame.display.set_mode((width, height))