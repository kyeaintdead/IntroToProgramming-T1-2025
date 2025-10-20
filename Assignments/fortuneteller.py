import random 
def fortuneteller():
    fortune = input("I am a fortune teller give me random numbers to tell your fortune type ok to proceed\n>")
    fortune = int(input("Give me your lucky number\n>"))
    if fortune >= random.randint(1, 100): 
        print("The future is favorable for you")
    else:
        print("The future is looking grim for you")
    fortune = float(input("How many years do you want to see in the future\n>"))
    if fortune >= random.uniform(1, 100):
        print("so and so will happen")
    else:
        print("So not so will happen")
    fortune = float(input("Give me a magical multiplier"))
    if fortune >= 14.6:
        print("You will die")
    else: 
        print("You lived nice!")

        
fortuneteller()