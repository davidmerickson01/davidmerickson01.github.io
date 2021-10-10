# classes
import pygame
import random
import math
from pygame.locals import *

class Creature:
    def point_value(self):
        # TODO: support more creatures
        if self.type == 0:
            # bug is good
            return 1
        else:
            # bird is bad
            return -1
        
    def move(self):
        # TODO: support different types of movement
        self.counter += 0.04
        if self.direction == 1:
            self.rect.x = self.center + math.sin(self.counter) * 200
        else:
            self.rect.y = self.center + math.sin(self.counter) * 100
            
    def draw(self, window, screen_x):
        window.blit(self.image,
            Rect(self.rect.x - screen_x, self.rect.y,
                 self.rect.width, self.rect.height))
        
    def __init__(self, world_width, world_height):
        # TODO: better graphics
        files = ("ladybug.png", "ladybug.png")
        self.type = random.randint(0,len(files)-1)
        
        self.image = pygame.image.load(files[self.type])
        w = self.image.get_rect().width
        h = self.image.get_rect().height
        self.rect = Rect(
            random.randint(0, world_width-w), random.randint(0, world_height-h),
            w, h)
        self.direction = random.randint(0, 1)
        if self.direction == 1:
            self.center = self.rect.x
        else:
            self.center = self.rect.y
        self.counter = random.randint(0,10) / 10
