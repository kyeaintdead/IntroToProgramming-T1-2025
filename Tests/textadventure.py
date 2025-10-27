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
print("WARNING. This game is heavily dark and relys on careful choice making. A simple choice can change your route for the worst, but this game doesn't have any wrong choices")
print("The Ultimate goal of the game is to return back to your previous world since in this setting you have been transported in a alternate world with horrors")
money = 0
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
    
    print("1. Investigate him")

    choice = input("> ")
    if choice == "1":
        gluttony_bad()                        # this leads to entrance to the gluttony route into the true ending
    else:
        print("Invalid. Try again")
        start_discard()





def gluttony_bad():
    while True:
        print("You try to stalk the man he instantly spots you. He goes over to you and then .... Who am I?")
        print("1. My name My name My name")
        print("2. Whole again....")
        print("3. I am...")

        choice = input("> ")

        if choice == "1":
            print("Who am I?")
            
        elif choice == "2": 
            print("Colors.... Colors....")
            
        elif choice == "3":
            print("I am " + name + "...")
            gluttony_sorrow()
            break   
            
        else:
            print("Invalid. Try again")
       

def gluttony_sorrow():
    while True:
        print("Your starving almost to the point where your stomach is dangerously close to sticking to your back how dangerous... how dangerous...")
        print("1. Look at a mirror")
        print("2. Look at a mirror")
        print("3. Look at a mirror")
        
        choice = input("> ")
        if choice == "1":
            print("You look different, malformed")
        elif choice == "2":
            print("You feel hungry")
        elif choice == "3":
            print("You smash the mirror. It's time to get something to eat, I need a weapon first")
            gluttony_plaza()
            break
        else:
            print("Invalid. Try again")

def gluttony_plaza():
    print("You have to get a weapon. You arrive at the plaza and go to the weapons dealer. What will you do to him")
    print("1. Ask him if he knows you")                       # trying to regain yourself route 
    print("2. Kill him and take a weapon")                    # alternative gluttony sub path, murder becomes a habit route 
    choice = input("> ") 
    if choice == "1":
        gluttony_dealer()
    elif choice == "2": 
        gluttony_dealer1()
    else:
        print("Invalid. Try again.")
        gluttony_plaza()

def gluttony_dealer1():
    print("You kill the weapons dealer and get a weapon. You feel yourself gain some sin")
    print("You realize you can the weapon to sever yourself from the man")
    print("Sever your relation with the man")
    choice = input("> ")
    if choice == "1":
        gluttony_severance()
    else:
        print("Invalid. Try again")




def gluttony_severance():
    print("SEVERANCE ENDING. You used your weapon and infused some of the sin you got from killing that man to sever the connection you had with the hooded man.")
    print("You regain your senses but after you severed the connection the hooded man swiftly kills you")





def gluttony_dealer():
    while True:
        print("He says he seen you around before and says your name " + name + " That triggers something in you...") 
        print("1. Kill him")
        print("2. Kill him")
        print("3. Kill him")
        choice = input("> ")
        if choice == "1":
            print("Take his memories")
        elif choice == "3":
            print("I need to find out who I am")
        elif choice == "2":
            print("I remember something about myself")
            gluttony_rememberance()
            break
        else:
            print("invalid. Try again")
            gluttony_dealer()

def gluttony_rememberance():
    while True:
        print("You feel sparks in your head, Your breathing is heavy, you feel nauseous, But suddenly you recall something")
        
        print("1. I am Arno Gratz")
        print("2. No I don't know what I'm gonna do next Arno")
        print("3. GET AWAY FROM ME")
        choice = input("> ") 
        if choice == "1":
            print("Hey " + name + " Your asking me if I seen you around?. Course I have! Hey why are you looking at me that way?")
            
        elif choice == "2":
            print("My name is Arno Gratz. I am 27 years old and I started selling weapons at the ripe age of 19. I'm soon to be married to my fiance I can't wait")
        elif choice == "3":
            print("I had many customers come and go looking different after a while but something seemed off about " + name + " today.")
            gluttony_recalling()
            break
        else:
            print("Invalid. Try again")
            
def gluttony_recalling():
    print("Seems like you discovered that you can re live a persons life if you kill them. You remember the previous you talking to the shop keeper they seem nice. Why can I see Arno right beside me?")
    print("1. Visit Arnos fiance")
    print("2. Talk to Arno")
    choice = input("> ")
    if choice == "1":
        Arnos_fiance()
    elif choice == "2":
        Arno_Dialogue()
    else:
        print("Invalid. Try again")
        gluttony_recalling()


def Arno_Dialogue():
    while True:
        print("Arno: It's alright " + name + " I don't hold it against you. What you are seeing is just a mere apparation created from your mind from the memories you gained")
        print("1. I'm sorry Arno but it's for the best")
        print("2. Push forward")
        choice = input("> ")
        if choice == "1":
            print("You see Arno vanish from your vision. You must stay in control over yourself")
        elif choice == "2":
            gluttony_power()
        else:
            print("Invalid. Try again")
            Arno_Dialogue()

            
def gluttony_power():
    print("From Arnos memories you find out the coordinates of a place that can lead you to power")
    print("1. Go to the watch tower")
    choice = input("> ")
    if choice == "1":
        watchtower()
    else:
        print("Invalid. Try again")
        gluttony_power()

def watchtower():
    print("You arrive at the watchtower and see a library. book shelves of filled with books all around you")
    print("You see some books you are interested in 2 especially. Which one do you read?")
    print("1. Book 1")
    print("2. Book 2")
    choice = input("> ")
    if choice == "1":
        I_am()
    elif choice == "2":
        Im_myself()
    else:
        print("Invalid. Try again")

def I_am():
    print("I AM ENDING. You read the book and relive another persons life. You felt like you actually were that person it felt kinda good. You began reading endless books in till you didn't even know who you were anymore")


def Im_myself():
    print("IM MYSELF ENDING. You chose the 2nd book and realize this is your book. You relive your entire life re claiming back your identity.")




def Arnos_fiance():
    print("With the memories of Arno you know exactly where his house is. You arrive at his house and find his fiance in the living room. Arno looks at you with a pleading look")
    print("1. Kill her")
    choice = input("> ")
    if choice == "1":
        Mending_Together()
    else:
        print("Invalid. Try again")
        Arnos_fiance()

def Mending_Together():                     # maybe add a alternative ending here 
    print("MENDING TOGETHER ENDING. After killing Arnos fiance you think of the real way to find yourself again is by killing others to regain your memory of your past self. Due to the killings you gained enough sin to be classified as chaotic you're both powerful and cold now. You go around the world asking others if they know you.")


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
        Heads_plaza()

def beggar_fire():
    print("You obtain a fire spell from the beggar. What will you do?")
    print("1. Use the fire spell")
    choice = input("> ")
    if choice == "1":
        fire_spell()
    else:
        print("Invalid. Try again")

def fire_spell():
    print("FIRE SPELL DEATH. Never take spells from strangers when you used the spell it exploded in your face")





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


def alleyway_help():
    print("You screamed for help and a person with orange hair clad with armor defends you against the bandits")
    print("He introduces himself at Ken and offers you a home since he sees you have nothing to your name accept?")
    print("1. Accept his offer")
    print("2. Decline")
    choice = input("> ")
    if choice == "1":
        help_ref()
    elif choice == "2":
        homeless_bum()
    else:
        print("Invalid. Try again")
        alleyway_help()


def homeless_bum():
    print("HOMELESS BUM ENDING. The man felt a little hurt and you walk away, turns out that was not the move you end up bumming around trying to keep yourself up but the opprotunitys just weren't in favor of you")



def help_ref():
    print("He brings you to his mansion. He asks if you have anywhere else to go and see you don't see he employs you as a worker at his house")
    print("1. Thank him")
    print("2. Plot")
    choice = input("> ")
    if choice == "1":
        employment_ending()
    elif choice == "2":
        plot_ending()
    else:
        print("Invalid. Try again")
        help_ref()

def employment_ending():
    print("EMPLOYMENT ENDING. You accept the mans request and become employed in his estate you lived your life peacefully with a nice income")

def plot_ending():
    print("PLOTTING ENDING. You accept the mans request but you secretly plot to kill the man so you can inherit his estate")
    print("After a few years you eventually poison the man and inherit his estate")




def plaza():
    print("You fled out of the alley way and arrived at the plaza")
    print("With nothing to your name you decide to find a job to get some money on your name")
    print("1. Take a job as a waiter at a local cafe")
    print("2. Take a job as a Adventurer")
    
    choice = input("> ")
    if choice == "1":
        waiter_job()
    elif choice == "2":
        Adventurer_job()
    else:
        print("Invalid. Try again")
        plaza()

def waiter_job():
    print("You decided to work for a couple of months at the cafe in till you had enough money to get a house and a steady living for yourself.")
    print("Since you have the resources now after gathering info for months you can do some research about a rumour of a way to transport to another world")
    print("1. Research Teleport")
    choice = input("> ")
    if choice == "1":
        waiter_ending()
    else:
        print("Invalid. Try again")
        waiter_job()

def waiter_ending():
    print("WAITER ENDING. You worked for a while at the cafe and used your combined research to build a portal to teleport to your original world")

def Adventurer_job():
    print("You got a job as a adventurer and worked for a bit killing monster and gaining orderly after you had enough orderly you could use the skill teleport")
    print("1. Teleport")
    choice = input("> ")
    if choice == "1":
        Adventurer_ending()
    else:
        print("Invalid. Try again")
        Adventurer_job()

def Adventurer_ending():
    print("HIGH ORDERLY ENDING.You became a high orderly and used the teleport to go back to your original world")







def Ruthless_pride():
    print("You decide to kill the three bandits with the stick you found on the ground. As you were cleaning off the blood off you spot a figure in a dark cloak. What will you do?")
    print("1. Try to kill him no witnesses aloud!")
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




def pride_death():
    print("EGO DEATH ENDING, Due to your own ego of thinking you're on top of the world you died! The hooded man was a powerful individual who was a chaotic, you met a untimely end")

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
    print("1. Sin")

    choice = input("> ")
    if choice == "1":
        pride_power()
    else:
        print("Invalid. Try again")
        pride_alone()


def pride_power():
    print("You realize you accumalated enough sin to become slighty chaotic. You can summon a fire spirit, you're fairly powerful now. What will you do?")
    print("1. Summon the fire spirit onto the town")
    print("2. Orderly")
    choice = input("> ")
    if choice == "1":
        fire_chaotic()
    elif choice == "2":
        fire_sacrfice()
    else:
        print("Invalid. Try again")
        pride_power()


def fire_chaotic():
    print("HIGH CHAOTIC ENDING. You used the fire spirit to burn down the whole Town. You gained even more sin resulting in you becoming a true chaotic.")


def fire_sacrfice():
    print("REDEMPTION ENDING. You felt bad for your past actions... You self atone and feel a flaming in your heart you feels your sins have been forgiven but... nothing comes without a cost. You felt relived with yourself as you were laying down on the cold ground feeling your heart beat get fainter")

    
        
    

def strength_regain():
    print("You find your hiding spot and sleep thinking how you got into this mess. A sudden scream awakes you and you see a woman getting robbed by bandits. What will you do?")
    print("1. Shes in trouble I have to help her")
    print("2. Screw her I'll stay hidden safe so I don't get hurt")
    print("3. Those bandits look useful I could use them to accomplish my goal. I'll go recruit them")
    choice = input("> ")
    if choice == "1":
        virtue_help()
    elif choice == "2":
        sloth_guilt()
    elif choice == "3":
        wrath_if()
    else:
        print("Invalid. Try again")
        strength_regain()


def sloth_guilt():
    print("You hide and see the woman get robbed. After a while you run away not wanting to be in that area")
    print("You feel paranoid so scared in fact you want to run away from this town")
    print("1. Move continents")
    choice = input("> ")
    if choice == "1":
        sloth()
    else:
        print("Invalid. Try again")
        sloth_guilt()

def sloth():
    print("PARANOID ENDING. You're constanstly scared of your surroundings after that day even to the point where you keep yourself up at night.")


def virtue_help():
    print("You saved the woman and she thanks you")
    print("You recieve some Money. What will you spend it on?")
    print("1. Some food")
    print("2. A weapon")
    choice = input("> ")
    if choice == "1":
        virtue_food()
    elif choice == "2":
        virtue_weapon()
    else:
        print("Invalid. Try again")
        virtue_help()




def virtue_weapon():                    # might need a global variable for a weapon here 
    print("You obtained the weapon")
    print("1. Go fight some bad guys")
    print("2. Resell the weapon")
    choice = input("> ")
    if choice == "1":
        badguy_virtue()
    elif choice == "2":
        resell_route()
    else:
        print("Invalid. Try again")
        virtue_weapon()

def badguy_virtue():
    print("You used your weapon to fight some bandits. You didn't kill them which gained you orderly")
    print("You could use some of your orderly to Teleport")
    print("1. Teleport")
    choice = input("> ")
    if choice == "1":
        print("TELEPORT ENDING?. You used Teleport to try to return to your original world but end up it an entirely different world.")

    else:
        print("Invalid. Try again")
        badguy_virtue()
        
def resell_route():
    print("RESELLING ENDING. You began reselling weapons in till you were immensely rich and you were able to live comfortably in the new world")




def virtue_food():
    print("You decide to use the money to buy some food. You arrive at the plaza and buy some. You see a beggar that looks hungry. What will you do?")
    print("1. Give food to the beggar")
    print("2. Eat the food in his face")
    choice = input("> ")
    if choice == "1":
        virtue_skill()
    elif choice == "2":
        cursed_route()
    else:
        print("Invalid. Try again")
        virtue_food()

def cursed_route():
    print("You ate the food infront of the beggar. The beggar starves to death. You don't feel any remorse but you feel like your heart is getting wrapped in thorns")
    print("You have been cursed by the beggars spirit you now walk with the thorns cursed. Anyone who interacts with you will feel immense pain if they come in a 30 feet radius of you")
    print("1. Lonesome")
    choice = input("> ")
    if choice == "1":
        Of_Thorns()
    else:
        print("Invalid. Try again")
        cursed_route()



def Of_Thorns():
    print("KING OF THORNS ENDING. After becoming cursed you lived a life of solitude. You decided living only a life of solitude wouldn't be fair to yourself so you take over a nation with your curse and become known as the King Of Thorns")
        




def virtue_skill():
    print("You decided to be generous and give some of your food to the beggar. He's very grateful and actually gives you a magical scroll")
    print("You used the magical scroll and obtained the spell Teleport")
    print("1. Teleport")
    choice = input("> ")
    if choice == "1":
        virtue_ending()
    else:
        print("Invalid. Try again")
        virtue_skill()


def virtue_ending():
    print("VIRTUE ENDING. You have been very generous throughout this journey, You used the spell Teleport and returned to your original world free from the suffering.")
start_fantasy()