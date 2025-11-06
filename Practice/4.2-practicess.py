
games = ["Elden Ring", "Shadow of", "Diablo III"]
for game in games:
    print(game)
    # print every number from 1 - 5 using a for loop 


for i in range(0,3):
    print("Rank " + str(i) + ":" + games[i])
#print every odd number from 1- 100
for i in range(1,100,9):
    print(i)    

# create a list of 100 random numbers that range from -100 to 100
#print only to positive numbers
import random
random_numbers = []
#for i in range(0, 100):
    #random_numbers.append(random.randint(-100, 101))
    #for num in random_numbers:
        #if num > 0:
            #print(random_numbers)

for i in range(0, len(random_numbers)):
    if random_numbers[i] < 0:
        random_numbers.pop(i)


print(random_numbers)

    