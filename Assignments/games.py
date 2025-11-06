def start_game():
    print("Welcome to the Adventure Game!")
    first_encounter()

def first_encounter():
    print("You find yourself at a crossroads.")
    choice = input("Do you want to go left (L) or right (R)? ").upper()
    if choice == 'L':
        encounter_two()
    elif choice == 'R':
        encounter_three()
    else:
        print("Invalid choice. Try again.")
        first_encounter()

def encounter_two():
    print("You encounter a mysterious old man.")
    choice = input("Do you want to talk to him (T) or ignore him (I)? ").upper()
    if choice == 'T':
        encounter_four()
    elif choice == 'I':
        encounter_five()
    else:
        print("Invalid choice. Try again.")
        encounter_two()

def encounter_three():
    print("You stumble upon a hidden cave.")
    choice = input("Do you want to enter the cave (E) or walk past it (W)? ").upper()
    if choice == 'E':
        encounter_six()
    elif choice == 'W':
        encounter_seven()
    else:
        print("Invalid choice. Try again.")
        encounter_three()

def encounter_four():
    print("The old man offers you a magical item.")
    choice = input("Do you accept it (A) or refuse it (R)? ").upper()
    if choice == 'A':
        encounter_eight()
    elif choice == 'R':
        encounter_nine()
    else:
        print("Invalid choice. Try again.")
        encounter_four()

def encounter_five():
    print("You walk away and find a treasure chest.")
    choice = input("Do you want to open it (O) or leave it (L)? ").upper()
    if choice == 'O':
        encounter_ten()
    elif choice == 'L':
        encounter_eleven()
    else:
        print("Invalid choice. Try again.")
        encounter_five()

def encounter_six():
    print("Inside the cave, you find a sleeping dragon.")
    choice = input("Do you want to sneak past it (S) or wake it up (W)? ").upper()
    if choice == 'S':
        encounter_twelve()
    elif choice == 'W':
        encounter_thirteen()
    else:
        print("Invalid choice. Try again.")
        encounter_six()

def encounter_seven():
    print("You find a hidden path leading to a village.")
    choice = input("Do you want to explore the village (E) or return (R)? ").upper()
    if choice == 'E':
        encounter_fourteen()
    elif choice == 'R':
        encounter_fifteen()
    else:
        print("Invalid choice. Try again.")
        encounter_seven()

def encounter_eight():
    print("You gain the ability to cast spells.")
    choice = input("Do you want to use it now (Y) or save it (N)? ").upper()
    if choice == 'Y':
        encounter_sixteen()
    elif choice == 'N':
        encounter_seventeen()
    else:
        print("Invalid choice. Try again.")
        encounter_eight()

def encounter_nine():
    print("You leave the old man and find a hidden path.")
    choice = input("Do you want to follow it (F) or ignore it (I)? ").upper()
    if choice == 'F':
        encounter_eighteen()
    elif choice == 'I':
        encounter_nineteen()
    else:
        print("Invalid choice. Try again.")
        encounter_nine()

def encounter_ten():
    print("You find gold coins inside the chest.")
    choice = input("Do you want to take them (T) or leave them (L)? ").upper()
    if choice == 'T':
        encounter_twenty()
    elif choice == 'L':
        encounter_twenty_one()
    else:
        print("Invalid choice. Try again.")
        encounter_ten()

def encounter_eleven():
    print("You walk away and find a hidden door.")
    choice = input("Do you want to open the door (O) or walk away (W)? ").upper()
    if choice == 'O':
        encounter_twenty_two()
    elif choice == 'W':
        encounter_twenty_three()
    else:
        print("Invalid choice. Try again.")
        encounter_eleven()

def encounter_twelve():
    print("You successfully sneak past the dragon.")
    choice = input("Do you want to explore further (E) or leave (L)? ").upper()
    if choice == 'E':
        encounter_twenty_four()
    elif choice == 'L':
        encounter_twenty_five()
    else:
        print("Invalid choice. Try again.")
        encounter_twelve()

def encounter_thirteen():
    print("The dragon wakes up and chases you!")
    choice = input("Do you want to fight (F) or run (R)? ").upper()
    if choice == 'F':
        encounter_twenty_six()
    elif choice == 'R':
        encounter_twenty_seven()
    else:
        print("Invalid choice. Try again.")
        encounter_thirteen()

def encounter_fourteen():
    print("You meet friendly villagers.")
    choice = input("Do you want to help them (H) or leave (L)? ").upper()
    if choice == 'H':
        encounter_twenty_eight()
    elif choice == 'L':
        encounter_twenty_nine()
    else:
        print("Invalid choice. Try again.")
        encounter_fourteen()

def encounter_fifteen():
    print("You return to the crossroads.")
    first_encounter()

def encounter_sixteen():
    print("You cast a spell and defeat an enemy.")
    encounter_thirty()

def encounter_seventeen():
    print("You save your spell for a more dangerous encounter.")
    encounter_thirty_one()

def encounter_eighteen():
    print("You find a hidden treasure.")
    encounter_thirty_two()

def encounter_nineteen():
    print("You wander aimlessly and get lost.")
    encounter_thirty_three()

def encounter_twenty():
    print("You become rich and powerful.")
    end_game()

def encounter_twenty_one():
    print("You leave the treasure behind and continue your journey.")
    end_game()

def encounter_twenty_two():
    print("You discover a secret passage.")
    encounter_thirty_four()

def encounter_twenty_three():
    print("You walk away and find a new adventure.")
    end_game()

def encounter_twenty_four():
    print("You find a magical artifact.")
    end_game()

def encounter_twenty_five():
    print("You escape safely but with no treasure.")
    end_game()

def encounter_twenty_six():
    print("You bravely fight the dragon and win!")
    end_game()

def encounter_twenty_seven():
    print("You escape but are injured.")
    end_game()

def encounter_twenty_eight():
    print("You help the villagers and gain their trust.")
    end_game()

def encounter_twenty_nine():
    print("You leave the village and continue your journey.")
    end_game()

def encounter_thirty():
    print("You become a hero in the land.")
    end_game()

def encounter_thirty_one():
    print("You prepare for the next challenge.")
    end_game()

def encounter_thirty_two():
    print("You become the wealthiest adventurer.")
    end_game()

def encounter_thirty_three():
    print("You find your way back home.")
    end_game()

def encounter_thirty_four():
    print("You uncover the secrets of the ancient world.")
    end_game()

def end_game():
    print("Thank you for playing the Adventure Game!")
    exit()

if __name__ == "__main__":
    start_game()