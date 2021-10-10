import pygame
from pygame.locals import *

box_width = 30
box_height = 50

class Platform:
    
    # TODO: different letters can be different things, make bigger world
    world = [
        "                                   OOO                      ",
        "          XXXX                    XXXXX         XXXXX       ",
        "                                                            ",
        "XXXXXXXXXXXXXXXXXXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXX       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"];

    # convert pixel x,y to world x,y
    def world_coord(self, pixel_x, pixel_y):
        world_x = int(pixel_x) // box_width
        world_y = int(pixel_y - (self.screen_height - self.world_height*box_height)) // box_height
        return (world_x, world_y)

    # convert world x,y to pixel x,y
    def pixel_coord(self, world_x, world_y):
        pixel_x = world_x * box_width
        pixel_y = self.screen_height - ((self.world_height - world_y) * box_height)
        return (pixel_x, pixel_y)
    
    # These functions check if mario collides with world boxes
    def point_collision(self, pixel_x, pixel_y):
        (world_x, world_y) = self.world_coord(pixel_x,pixel_y)
        return world_x < self.world_width and \
               world_y >= 0 and world_y < self.world_height and \
               self.world[world_y][world_x] != ' '

    def rect_collision(self, r, x_inc, y_inc):
        left = r.x
        top = r.y
        right = r.x + r.width
        bottom = r.y + r.height
        return self.point_collision(left + x_inc, top + y_inc) or \
               self.point_collision(right + x_inc, top + y_inc) or \
               self.point_collision(left + x_inc, bottom + y_inc) or \
               self.point_collision(right + x_inc, bottom + y_inc)

    def box_color(self, x, y):
        box = self.world[y][x]
        if box == 'X':
            color = (128,128,128)
        elif box == 'O':
            color = (44,128,44)
        else:
            color = (128,255,128)
        return color

    def draw(self, windowSurface, screen_x):
        for y in range(self.world_height):
            for x in range(self.world_width):
                if self.world[y][x] != ' ':
                    (pixel_x, pixel_y) = self.pixel_coord(x, y)
                    windowSurface.fill(self.box_color(x,y),
                        # -1 allows a little of a background to show through
                        Rect(pixel_x - screen_x, pixel_y, box_width-1, box_height-1))

    def collision(self, mario_rect, x_inc, y_inc):
        # check if mario hits world[] by testing movement in x and y directions
        if y_inc != 0 and \
           self.rect_collision(mario_rect, x_inc, y_inc) and \
           (not self.rect_collision(mario_rect, x_inc, 0) or not self.rect_collision(mario_rect, 0, 0)):
            y_inc = 0
        if x_inc != 0 and \
           self.rect_collision(mario_rect, x_inc, y_inc) and \
           not self.rect_collision(mario_rect, 0, y_inc):
            x_inc = 0
        return (x_inc, y_inc)

    def __init__(self, screen_height):
        self.screen_height = screen_height
        self.world_height = len(self.world)
        self.world_width = len(self.world[0])
        
