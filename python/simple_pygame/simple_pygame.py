# https://www.pygame.org/
import pygame, sys, time
from pygame.locals import *

guy = pygame.image.load('guy.png')
background = pygame.image.load('background.jpg')

windowSurface = pygame.display.set_mode((background.get_width(), background.get_height()),0,32)
pygame.display.set_caption('simple pygame')

guy_rect = pygame.Rect(
    background.get_width()/2, background.get_height()/2,
    guy.get_width(), guy.get_height())

inc_x = 0
inc_y = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                inc_x = -5
            elif event.key == K_RIGHT:
                inc_x = 5
            elif event.key == K_UP:
                inc_y = -5
            elif event.key == K_DOWN:
                inc_y = 5
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                inc_x = 0
            elif event.key == K_UP or event.key == K_DOWN:
                inc_y = 0

    guy_rect.x += inc_x
    guy_rect.y += inc_y

    #windowSurface.fill((121,214,52))
    windowSurface.blit(background, background.get_rect())

    #pygame.draw.rect(windowSurface, (255,0,0), guy_rect)
    windowSurface.blit(guy, guy_rect)

    pygame.display.update()
    time.sleep(0.02)
