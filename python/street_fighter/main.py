# import the modules we need
import pygame
import random
import os
import player_stat
import time

# initialize all the pygame modules
pygame.init()

# initialize the window for the game
win = pygame.display.set_mode((720,480))

# load images
# per the pygame docs, os.path.join() should be used for compatibility
guy = pygame.image.load(os.path.join("assets", "guy1.png"))

guy_punch = [
    pygame.image.load(os.path.join("assets", "guy_punch0.png")),
    pygame.image.load(os.path.join("assets", "guy_punch1.png")),
    pygame.image.load(os.path.join("assets", "guy_punch2.png"))
]

boss = [
    pygame.image.load(os.path.join("assets", "boss0.png")),
    pygame.image.load(os.path.join("assets", "boss1.png"))
]
background = pygame.image.load(os.path.join("assets", "background2.jpg"))

# set the caption at the top of the window
pygame.display.set_caption("Street Fighter: punch")

font = pygame.font.SysFont("comicsansms", 30)

floor_y = 400
score = 0
lives = 3

def set_initial_positions():
    global guyrect, bossrect
    guyrect = pygame.Rect(50, floor_y-guy.get_height(),guy.get_width(), guy.get_height())
    bossrect = pygame.Rect(300,floor_y-200,100,200)

set_initial_positions()

guyHealth = player_stat.PlayerStat("health", (255,255,255))
bossHealth = player_stat.PlayerStat("health", (0,255,0))

# 0 = nothing
# 1 = move right
# 2 = move left
# 3 = jump
bossmove = 0
bosscounter = 50
punch_index = 0

def do_user_input():
    global guyrect, punch_index
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                punch_index = 1
            elif event.key == pygame.K_a:
                guyrect = guyrect.move(-15,0)
            elif event.key == pygame.K_d:
                guyrect = guyrect.move(15,0)
    return True

def move_boss():
    global bosscounter, bossrect, bossmove, bossjump
    if bosscounter > 0:
        bosscounter -= 1
    else:
        bossmove = random.randint(0,3)
        print(bossmove)
        if bossmove == 1:
            bosscounter = 5
        elif bossmove == 2:
            bosscounter = 5
        elif bossmove == 3:
            bosscounter = 50
            bossjump = -30
    
    if bossmove == 1:
        if bossrect.x + bossrect.width < 720:
            bossrect = bossrect.move(20,0)
    elif bossmove == 2:
        if bossrect.x > 0:
            bossrect = bossrect.move(-20,0)
    elif bossmove == 3:
        bossrect = bossrect.move(0,bossjump)
        bossjump += 6
        if bossrect.y + bossrect.height == floor_y:
            bossmove = 0
            bosscounter = 0

def draw_scene():
    #win.fill((255,255,255))
    #win.fill((0,0,0), (0,floor_y,720,480-floor_y))
    win.blit(background, (0,0,720,480))
    for x in range(lives):
        win.fill((0,255,0), (600+x*20,10,10,10))

def draw_guy():
    global punch_index
    if punch_index > 0:
        # punch_index can be 1,2,3
        win.blit(guy_punch[punch_index-1], guyrect)
        # go to the next image in the punch
        punch_index += 1
        if punch_index == 4:
            punch_index = 0
    else:
        win.blit(guy, guyrect)

def draw_boss(impact = False):
    if impact:
        bossindex = 1
    else:
        bossindex = 0
    win.blit(boss[bossindex], bossrect)

def inner_loop():
    global score
    if not do_user_input():
        return False
    move_boss()
    draw_scene()
    draw_guy()


    impact = False
    if guyrect.colliderect(bossrect) and punch_index > 0:
        # good
        score += 10
        bossHealth.decrease(10)
        impact = True
    elif guyrect.colliderect(bossrect):
        # bad
        if random.randint(1,100) <= 10: # 10%
            guyHealth.decrease(5)
    elif punch_index == 3:
        # bad
        guyHealth.decrease(1)
    #else
        # no punch, no collide, nothing

    draw_boss(impact)

    # draw score
    text = font.render("Score: " + str(score), True, (0, 128, 0))
    win.blit(text, (100,100,0,0))

    guyHealth.drawBar(win,  300, 50, 200, 30)
    bossHealth.drawBar(win, 300, 100, 200, 30)

    pygame.display.update()
    pygame.time.delay(100) # millisecond, 10 frames per second
    return True

def postMessage(text):
    text = font.render(text, True, (0,0,0))
    win.blit(text, (300,200,0,0))
    pygame.display.update()
    time.sleep(3)

# main program
playAgain = True
while playAgain:
    lives = 3

    draw_scene()
    draw_guy()
    draw_boss()
    postMessage("The match begins...")
    
    while lives > 0 and playAgain:
        set_initial_positions()
        bosscounter = 0
        bossjump = 0
        bossmove = 0

        draw_scene()
        draw_guy()
        draw_boss()
        postMessage("Life " + str(lives))

        bossHealth.reload()
        guyHealth.reload()
       
        while not (bossHealth.isEmpty() or guyHealth.isEmpty()) and playAgain:
            if not inner_loop():
                playAgain = False
                
        if playAgain == True:
            if guyHealth.isEmpty():
                postMessage("You are dead. Next life...")
                lives = lives - 1
            else:
                postMessage("You win! Next round...")
    if playAgain:
        postMessage("You are out of lives. Play again?")
        answer = input()
        playAgain = (answer[0] == 'y')

pygame.quit()
