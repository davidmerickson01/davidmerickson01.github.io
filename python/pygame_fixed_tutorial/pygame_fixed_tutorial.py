# fixes to https://www.pygame.org/docs/tut/PygameIntro.html
import sys, pygame
import time

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
# renamed variable so it can be changed
background_color = (0,0,255)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # added this to actually exit
            pygame.quit()
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background_color)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    # added sleep to get 50fps
    time.sleep(0.02)
