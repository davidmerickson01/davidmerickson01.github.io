import pygame, sys, time
import random
import creature_class, platform_class
from pygame.locals import *

pygame.init()

screen_height = 400
screen_width = screen_height // 9 * 16
windowSurface = pygame.display.set_mode((screen_width, screen_height),0,32)
pygame.key.set_repeat(1)
pygame.display.set_caption('Simple Mario')
background = pygame.image.load('background.png')
background_width = background.get_rect().width
mario_image = pygame.image.load('Mario-left-big-still.png')
# TODO: need better graphics for mario, bugs and world, blocks

# position of mario in global coordinates
mario_rect = pygame.Rect(screen_width//2 - 15, 80, 30, 60)

platform = platform_class.Platform(screen_height)

# list of bugs on screen
bugs = []
def create_bug():
    creature = creature_class.Creature(background_width, screen_height)
    bugs.append(creature)
for i in range(5):
    create_bug()

points = 0
x_inc = 0
y_inc = 0
# screen_x is the position of the left edge of the screen in
# the global coordinate system
screen_x = 0
prev_screen_x = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            # TODO: other keys for other actions
            if event.key == K_LEFT:
                # change in velocity is acceleration
                if x_inc > -8:
                    x_inc -= 2
            elif event.key == K_RIGHT:
                if x_inc < 8:
                    x_inc += 2
            elif event.key == K_UP:
                # jump - a burst of upward acceleration
                y_inc = -10

    # gravity - constant downward acceleration
    y_inc += 1.5
    
    # world and screen bounds (4x the background)
    if screen_x + x_inc <= 0 or screen_x + x_inc >= background_width * 4:
        x_inc = 0
    if mario_rect.y + y_inc <= 0 or mario_rect.y + y_inc + mario_rect.height >= screen_height:
        y_inc = 0

    # check for collision with platform
    (x_inc, y_inc) = platform.collision(mario_rect, x_inc, y_inc)

    # move screen and mario
    screen_x += int(x_inc)
    mario_rect.x += int(x_inc)
    mario_rect.y += int(y_inc)

    # check for collision with bugs
    for bug in bugs[:]:
        bug.move()
        if mario_rect.colliderect(bug.rect):
            bugs.remove(bug)
            # TODO: need uncompressed WAV for sound effect
            #pygame.mixer.Sound.play(swoosh_sound)
            points += bug.point_value()
            create_bug()

    # draw left-side background using modulus to allow continuous wrapping
    width = (background_width - screen_x%background_width)
    windowSurface.blit(background,
        Rect(0,0,width, screen_height),
        Rect(screen_x%background_width,0,width, screen_height))
    # draw right-side background if needed
    if screen_x > background_width - screen_width:
        x = background_width - screen_x%background_width
        width = screen_width - x
        windowSurface.blit(background,
            Rect(x,0,width,screen_height),
            Rect(0,0,width,screen_height))

    # draw platform, bugs and mario
    platform.draw(windowSurface, screen_x)           
    for bug in bugs:
        bug.draw(windowSurface, screen_x)
    windowSurface.blit(mario_image,
        Rect(mario_rect.x - screen_x, mario_rect.y, mario_rect.width, mario_rect.height))

    # TODO: use font to draw points, lives, etc.

    pygame.display.update()
    time.sleep(0.02)
