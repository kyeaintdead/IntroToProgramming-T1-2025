# How the story is gonna go is that you wake up in a alley way 
#you have to survive in this fantasy world since you are homeless and don't know where to go
# there will be around 7 paths that you can do and these will be the seven deadly sins
# the goal is for the player to acheive the ending where they dont end up consumed in sin
# mutiple encounters will lead to these endings 
#pride route will involve the player into joining a assassin cult where they will become a wanted assassin 
#pride route continued. Due to the players pride of thinking they don't need help they will receive the pride route ending. all they need is themselves
#wrath route will involve the player in needing a key item throughout the game that will be the coin
#wrath route continued. The player will soley use the coin for decision making and eventually becoming a mob boss or being betrayed
#sloth route initation is the player has to only think about themselves in a cowardly way
#sloth route continued. the player will eventually run away and live a normal life but won't be able to truely be happy
#gluttony route will involve the player in being poessed by a strange man forcing them to lose their memorys
#gluttony route continued. the player will have to re piece there memorys by going around the world
#greed intitation is for the player to also have the coin but eventually discard for something better
#greed will have the player acting selfishly for their own benefit 
# true route. the player will have to make careful choices for others and themselves in order to acheive true happiness
name = input("What is your name? \n> ")
copper_coin = "1"
def start_fantasy():
    print("You just woke up in a alley way exhausted. What will you do:")
    print("1. Look around see if theres any people")
    print("2. Find a hiding spot and Rest up regain your energy and think of the predicament you are in")
    print("3. Pick up the random coin on the ground could be useful")
    
    choice = input("> ")

    if choice == "1":
        bandit_fight()           # 1 sin route in this encounter 
    elif choice == "2":
        strength_regain()
    elif choice == "3":
        coin_route()
    else:
        print("Invalid you can not escape fate. Try again.")
        start_fantasy()

def coin_route():
    print("After obtaining the coin you feel ominous and grim")
    print("1. Heads")
    print("2. Tails ")
    print("3. Discard coin")
    
    choice = input("> ")
    if choice == "1":
        Heads_plaza()
    elif choice == "2":
        Tails_plaza()
    elif choice == "3":
        start_discard()
    else:
        print("Invalid. Try again")
        coin_route()


def start_discard():
    print("You discarded the coin. You feel a wave of relief. You see a hooded man and feel drawn to him. What will you do?")
    print("1. Talk to him")
    print("2. Investigate him")

    choice = input("> ")
    if choice == "1":
        gluttony_good()                             # this leads to entrance to the gluttony route into the true ending
    elif choice == "2":                             # this is the entrance to the alternate gluttony route 
        gluttony_bad()
    else:
        print("Invalid. Try again")

def gluttony_bad():
    print("You try to stalk the man he instantly spots you. He goes over to you and then .... Who am I?")
    print("1. My name My name My name")
    print("2. Whole again....")
    print("3. I am...")
          
    
    choice = input("> ")
    if choice == "1":
        print("Who am I?")
        gluttony_bad()
    elif choice == "2": 
        print("Colors.... Colors....")
       
    elif choice == "3":
        print("I am " + name)
        gluttony_sorrow()
    else:
        print("Invalid. Try again")
        gluttony_bad()





def Heads_plaza():
    print("So you have chosen heads?. You will be forced to take a kinder approach to things. You arrive at the plaza and see a beggar. What will you do?")
    print("1. Buy him some food")
    print("2. Give him some cash")
    print("3. Give him your life savings")

    choice = input("> ")
    if choice == "1":
        beggar_fire()
    elif choice == "2":
        beggar_dagger()
    elif choice == "3":
        beggar_teleport()
    else:
        print("Invalid. Try again")
        Heads_plaza

def Tails_plaza():
    print("So you have chosen Tails... You will take a much more brutal approach on things. You arrive at the plaza and see a beggar. What will you do?")
    print("1. Bash his head in")
    print("2. Steal his stuff")
    print("3. Report him the beggar for stealing")
    choice = input("> ")
    if choice == "1":
        sin_achieved()
    elif choice == "2":
        beggar_belongings()
    elif choice == "3":
        blood_money()
    else:
        print("Invalid Try again.")
        Tails_plaza()

def bandit_fight():
    print("You see three suspicous people eyeing you weridly. Looks like they're picking a fight. What will you do:")
    print("1. Run away it's not worth my life")
    print("2. You see a stick on the ground you can use to hurt them. It's either me or them")
    print("3. Scream for help")

    choice = input("> ")
    if choice == "2":                # Pretty much down the pride route if you pick this option can still get a different route but not a good one 
        Ruthless_pride()
    elif choice == "1":
        plaza()
    elif choice == "3":
        alleyway_help()
    else:
        print("Invalid. Try again")
        bandit_fight()

def Ruthless_pride():
    print("You decide to kill the three bandits with the stick you found on the ground. As you were cleaning off the blood off you spot a figure in a dark cloak. What will you do?")
    print("1. Try to kill him no witnesses aloud")
    print("2. Run away. I can't get caught yet!")
    print("3. Go up to the figure and ask if he saw what you did")
    
    choice = input("> ")
    if choice == "3":
        pride_Assassin()             # fully lost it no redemption the person is now down the pride route
    elif choice == "2":
        inevitable_sloth()           # might lead to the sloth route still redeemable
    elif choice == "1":
        pride_death()                 # Death ending 
    else:
        print("Invalid. Try again") 
        Ruthless_pride()

def pride_Assassin():
    print("The hooded man says he did!. He saw your combat abilitys and ruthlessness, he wishes to recruit you to some Assassin cult. Any questions?. What will you ask him:")
    print("1. Whats in it for me?")
    print("2. Ignore him. Seems like another lunatic")
  
    choice = input("> ")
    if choice == "1":
        pride_joined()
    elif choice == "2":                # this choice diverges the pride route into 2 paths, either ignore him and find your own way or join them and become apart of the cult 
        pride_alone()
    else:
        print("Invalid. Try again")
        pride_Assassin()

def pride_joined():
    print("You will be able to gain power, riches, anything you want can be yours all you have to do is join us!")
    print("1. Sounds good to me i'll join")
    choice = input("> ")
    if choice == "1":
        pride_ending()
    else:
        print("Invalid. Try again")
        pride_joined()

def pride_ending(): 
    print("PRIDE ENDING, You ended up accepting the hooded mans deal and joined the Assassin cult you went around doing jobs in order to get money becoming a serial killer feared throughout the world. Due to your ego you decided the life you were living is okay because you had confidence in yourself")
    

def pride_alone():
    print("After ignoring the strange man you decide to go off on your own")
    print("1. Go to the plaza")
    print("2. Go outside of the town")
    print("Summon ")  
    
     
    

def strength_regain():
    print("You find your hiding spot and sleep thinking how you got into this mess. A sudden scream awakes you and you see a woman getting robbed by bandits. What will you do?")
    print("1. Shes in trouble I have to help her")
    print("2. Screw her I'll stay hidden safe so I don't get hurt")
    print("3. Those bandits look useful I could use them to accomplish my goal. I'll go recruit them")
start_fantasy()