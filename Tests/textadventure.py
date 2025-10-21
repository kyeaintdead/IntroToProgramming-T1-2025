# How the story is gonna go is that you wake up in a alley way 
#you have to survive in this fantasy world since you are homeless and don't know where to go
# there will be around 7 paths that you can do and these will be the seven deadly sins
# the goal is for the player to acheive the ending where they dont end up consumed in sin
# mutiple encounters will lead to hese endings 
def start_fantasy():
    print("You just woke up in a alley way exhausted. What do you do:")
    print("1. Look around see if theres any people")
    print("2.  Find a hiding spot and Rest up regain your energy and think of the predicament you are in")
    print("3. Pick up the random coin on the ground could be useful")
    
    choice = input("> ")

    if choice == "1":
        bandit_fight()
    elif choice == "2":
        strength_regain()
    elif choice == "3":
        wrath_possible()
    else:
        print("Invalid you can not escape fate. Try again.")


def bandit_fight():
    print("You see three suspicous people eyeing you weridly. Looks like they're picking a fight. What will you do:")
    print("1. You see a stick on the ground you can use to hurt them. It's either me or them")
    print("2. Run away it's not worth my life")
    print("3. Scream for help")

    choice = input("> ")
    if choice == "1":
        Ruthless_pride()
    elif choice == "2":
        plaza()
    elif choice == "3":
        alleyway_help()
    else:
        print("Invalid. Try again")

def strength_regain():
    print("You find your hiding spot and sleep thinking how you got into this mess. A sudden scream awakes you and you see a woman getting robbed by bandits. What do you do?")
    
start_fantasy()