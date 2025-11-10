import random 

secret_num = random.randint(1,100)
guess = 0
while guess != secret_num:
    try:
        guess = input(int("Guess the number between 1 and 100"))
    except:
        guess =+ 1
        if secret_num >= guess:
            print("Too high")
        elif secret_num <= guess:
            print("Too low")