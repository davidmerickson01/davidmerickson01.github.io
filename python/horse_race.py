import random

print("Horse race!")

num_horses = int(input("How many horses will be in the race?"))

# create two empty lists: horse names and horse distances
names = list()
distances = list()

# now populate the lists with the horses and their starting distance
# for example, range(3) will produce (0,1,2), then i will iterate through that
for i in range(num_horses):
    names.append(input("What is the name of horse #"+str(i+1)+"?"))
    distances.append(0)

print("Are you ready to race? Press ENTER to start.")
input()
print("Here we go...")

done = False
winning_horse = 0
while not done:
    input("Press enter for the next lap")
    
    for i in range(num_horses):
        # you are competing with randomness!
        distances[i] += random.randint(0, 40)
        if distances[i] > distances[winning_horse]:
            winning_horse = i
        # it's a 200 yard race, so the first one past ends the race
        if distances[i] >= 200:
            done = True

    if done:
        break

    for i in range(num_horses):
        print(names[i] + " is at " + str(distances[i]) + " yards",end='')
        if i == winning_horse:
            print(" and is in the lead!")
        else:
            print()
    print()

print(names[winning_horse]+" is the winner!")

input("Press ENTER to exit")
