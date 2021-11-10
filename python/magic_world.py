import time

print("Magic World")

objects = ["a sword","a magic shield","a ring"]

done = False
while not done:
    print("You are walking through the woods")
    print("And you see...")
    for i in range(len(objects)):
        print(i,":",objects[i])

    print("What do you want to pick up?")
    choice = int(input())

    print("You have picked up " + objects[choice])

    if choice == 0:
        print("You are warrior.")
        time.sleep(1)
        print("A goblin comes...")
        time.sleep(1)
        print("You stab him")
    elif choice == 1:
        print("Sorry. You're dead because the shield is toxic.")
    else:
        answer = input("Do you know any eligible maidens?")
        # by using lower() and [0], you can answer: Yes, yes, Y or y
        if answer.lower()[0] == 'y':
            print("Tt's time to propose!")
        else:
            print("So sad.")
    answer = input("Do you want to play again?")

    # done means not "yes". think about how this works.
    done = not (answer.lower()[0] == 'y')
