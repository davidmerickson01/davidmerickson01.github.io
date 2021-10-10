import random;

print("Football")

# This is a really simple version of the game
# What is missing or wrong?
# Yardage is just 0 to 100, not 0 to 50, then 50 to 0
# There's only one score
# There are no punts or field goals or extra points
# There are no fumbles or interceptions
# What else? How can you add some of these things? Or what other game can you make?

down = 1
down_yardage = 10
field_position = 20
score = 0
num_plays = 0

while num_plays < 40:
    switch = False
    num_plays = num_plays + 1
    down_string = ["","1st","2nd","3rd","4th"]
    print("It's",down_string[down],"and",down_yardage,"at the",field_position,"yard line")
    print("Pick a play: [r]un or [p]ass")
    play = input()
    if play == 'r':
        gain = random.randint(-3, 15)
        if gain >= 0:
            print("You gained",gain,"yards")
        else:
            print("You lost",-gain,"yards")
        field_position += gain
        down_yardage -= gain
        if field_position >= 100:
            print("Touchdown!")
            score += 7
            switch = True
    elif play == 'p':
        if random.randint(0,100) < 30:
            gain = 0
        else:
            gain = random.randint(0,20)
        if gain == 0:
            print("Incomplete")
        elif gain > 0:
            print("You gained",gain,"yards")
        else:
            print("You lost",-gain,"yards")
        field_position += gain
        down_yardage -= gain
        if field_position >= 100:
            print("Touchdown!")
            score += 7
            switch = True

    if switch:
        down = 1
        down_yardage = 10
        print("The other team gets the ball")
    else:
        if down_yardage <= 0:
            print("First down!")
            down = 1
            down_yardage = 10
        else:
            down += 1
            if down > 4:
                down = 1
                down_yardage = 10
                print("The other team gets the ball")

print("The game is over")
