
while True:
    name = input("What is your name? \n> ").strip()
    if not name:  
        print("You must enter a name.")
    elif name.isdigit():  
        print("Names cannot be numbers. Try again.")
    else:
        break
print("Your name is:", name)
print("WARNING. This game is heavily dark and relys on careful choice making. A simple choice can change your route for the worst, but this game doesn't have any wrong choices")
print("The Ultimate goal of the game is to return back to your previous world since in this setting you have been transported in a alternate world with horrors")
print("This game follow aspects of the seven deadly sins. Will you fall to sin or succeed in virtue?")
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





def gluttony_bad():        #check this for later
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
    print("You realize you can use the weapon to sever yourself from the man")
    print("1. Imbue your weapon with chaotic and sever your relation with the man")
    choice = input("> ")
    if choice == "1":
        gluttony_severance()
    else:
        print("Invalid. Try again")
        gluttony_dealer1()




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
            break
        else:
            print("Invalid. Try again")
            

            
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
    print("You see some books you are interested in 1 and 2 especially. Which one do you read?")
    print("1. Book 1")
    print("2. Book 2")
    choice = input("> ")
    if choice == "1":
        I_am()
    elif choice == "2":
        Im_myself()
    else:
        print("Invalid. Try again")
        watchtower()

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


def beggar_teleport():
    print("The beggar thanks you and gives you a teleport scroll use it?")
    print("1. Yes")
    print("2. No")
    choice = input("> ")
    if choice == "1":
        tp_void()
    elif choice == "2":
        kept_tp()
    else:
        print("Invalid. Try again")
        beggar_teleport()


def tp_void():
    print("VOID ENDING. You teleported in a black space no sound or light is here only void")


def kept_tp():
    print("DUMB ENDING. You have one chance to use the teleport scroll and you said no?")


def beggar_dagger():
    print("You purchased a dagger")
    print("1. Heads")
    print("2. Tails")
    choice = input("> ")
    if choice == "1":
        heads_dagger()
    elif choice == "2":
        tails_dagger()
    else:
        print("Invalid. Try again")
        beggar_dagger()




def tails_dagger():
    print("So you have chosen tails. You will be forced to take a more brutal approach on things")
    print("1. Use the dagger.")
    print("2. Rob someone")
    choice = input("> ")
    if choice == "1":
        chaotic_pathway()
    elif choice == "2":
        robbing()
    else:
        print("Invalid. Try again")
        tails_dagger()

def chaotic_pathway():
    print("You began to viciously kill everybody nearby gaining more chaotic for each kill.")
    print("You feel the coins influence on you has faded")
    print("In order for you to ascend you have to kill a orderly")
    print("You see one in the distance and you make your move")
    print("1. Imbue your dagger with chaotic")
    print("2. Use your chaotic to influence them")
    choice = input("> ")
    if choice == "1":
        chaotic_death()
    elif choice == "2":
        chaotic_pillar()
    else:
        print("Invalid. Try again")
        chaotic_pathway()


def chaotic_death():
    print("CHAOTIC DEMISE ENDING. Bad idea the orderly got the upper hand on you when they clashed with your dagger. You met an untimely end")

def chaotic_pillar():
    print("CHAOTIC PILLER ENDING. You killed the orderly and ascended as the epitome of chaotic. You're fine with the way things are and decide not to go back to your own world")


def robbing():
    print("JAIL ENDING. You robbed a person but got caught right after you sit here with a sentence of 20 years.")



def heads_dagger():
    print("So you have chosen heads. You will be forced to take a kinder approach on things. You use the dagger for what?")
    print("1. Go outside of town and clear out the monster infestation")
    print("2. Go to a dungeon")
    choice = input("> ")
    if choice == "1":
        monster_infestation()
    elif choice == "2":
        dungeon()
    else:
        print("Invalid. Try again")
        heads_dagger()


def dungeon():
    print("You arrive at the dungeon. Fight the boss?")
    print("1. Yes")
    print("2. No")
    choice = input("> ")
    if choice == "1":
        dungeon_boss()
    elif choice == "2":
        print("Nah, you gotta do it")
        dungeon()
    else:
        print("Invalid. Try again")  
        dungeon()

def dungeon_boss():
    print("BOSS ENDING. You fought and won against the boss nice")
        







def monster_infestation():
    print("You went to go clear out the monsters outside of the town. Your good deeds uplift you")
    print("You feel yourself becoming a orderly")
    print("You feel the coins influence on you fade away. You're much stronger now")
    print("1. Take on a chaotic")
    choice = input("> ")
    if choice == "1":
        chaotic_fight()
    else:
        print("Invalid. Try again")
        monster_infestation()

def chaotic_fight():
    print("You need to find a chaotic in order to become a pillar of strength in this world")
    print("You find a chaotic but hes already one step ahead of you")
    print("Death.")
    print("Death.")
    print("Death.")
    print("He's trying to brain wash you!. What will you do?")
    print("1. Imbue your dagger with some of your orderly and try to stab him")
    print("2. Use your orderly to cast a spell")
    choice = input("> ")
    if choice == "1":
       orderlyinsanity()
    elif choice == "2":
        highpillar()
    else:
        print("Invalid. Try again")
        chaotic_fight()

def highpillar():
    print("PILLAR OF THE WORLD ENDING. You defend against the brain wash and swiftly defeat the chaotic with one of your spells. You feel yourself ascending and become the epitome of orderly. You have the power to return to your world but your fine with this outcome")
    
def orderlyinsanity():
    print("LOST MAYHEM ENDING. You fail to defend against the brain washing and get defeated instead of you ascending the chaotic ascends as a higher being of chaotic. Who knows how doomed the world is now")
        

    


        
    

def beggar_fire():
    print("You obtain a fire spell from the beggar. What will you do?")
    print("1. Use the fire spell")
    choice = input("> ")
    if choice == "1":
        fire_spell()
    else:
        print("Invalid. Try again")
        beggar_fire()

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



def blood_money():
    print("You hand the guard a pouch heavy with coins. They jingle like tiny screams in the dead air.")
    print("The beggar looks at you, confused, hopeful — until they realize what you've done.")
    print("You framed them. You told the guards theyd stolen your coin.")
    print("The guards drag them away. Their pleas echo down the alley until silence devours them.")
    print()
    print("A week passes. A messenger finds you at the market.")
    print("'For your assistance in upholding justice,' he says, handing you a small sealed envelope.")
    print("Inside, thirty blood-red coins clink together. The metal smells like iron and regret.")
    print("You feel their weight. Its heavier than gold should be.")
    print()
    print("That night, you dream of the beggar — eyes hollow, mouth sewn shut with silver thread.")
    print("When you wake, your palms are stained red. You wash them, but the color wont fade.")
    print()
    print("1. Spend the blood money without hesitation.")
    print("2. Try to return it.")
    print("3. Flip the coin again — maybe fate will decide whats next.")
    choice = input("> ")

    if choice == "1":
        spend_blood_money()
    elif choice == "2":
        return_blood_money()
    elif choice == "3":
        fate_coin_flip()
    else:
        print("The wind answers instead. The coins rattle like teeth. You feel the world watching.")
        blood_money()

def spend_blood_money():
    print()
    print("You buy a new cloak, food, and drink. Every luxury dulls the sound of their scream.")
    print("But as you eat, you swear the taste of metal clings to your tongue.")
    print("Your gold pouch seems to whisper when you sleep — promising more, if you only reach deeper into your greed.")
    print()
    print("The more you spend, the less you feel. The less you feel, the more the coins whisper.")
    print("One morning, you wake to find every coin melted into your flesh — shining through your veins like molten light.")
    print("Your heart beats once... twice... and turns to gold.")
    print()
    print("You have become a statue of wealth — unmoving, eternal, adored by none.")
    print("The market dogs lick at your feet. They taste copper.")
    print()
    print("=== ENDING: THE GILDED CORPSE ===")
    print("Greed hollowed you out and filled the space with silence.")
    print()
    print("1. Restart")
    print("2. Exit")
    choice = input("> ")
    if choice == "1":
        start_fantasy()
    elif choice == "2":
        exit()
    else:
        spend_blood_money()

def return_blood_money():
    print()
    print("You walk to the guards’ hall, trembling. You leave the coins on their desk and whisper an apology.")
    print("No one listens. When you step outside, the world feels colder — but lighter.")
    print("A raven watches from the rooftop, and in its eye you see yourself reflected — small, but clean again.")
    print()
    print("You spend the rest of your life feeding the hungry, never touching gold again.")
    print("Sometimes, when you sleep, you still hear coins clinking in the dark.")
    print("But you never wake with blood on your hands.")
    print()
    print("=== ENDING: THE WEIGHT LIFTED ===")
    print("You broke the circle of greed, but its echo remains.")
    print()
    print("1. Restart")
    print("2. Exit")
    choice = input("> ")
    if choice == "1":
        start_fantasy()
    elif choice == "2":
        exit()
    else:
        return_blood_money()

def fate_coin_flip():
    print()
    print("You take out the same coin. It glints under the moonlight, half gold, half crimson.")
    print("You whisper: 'Heads — redemption. Tails — more blood.'")
    print("The coin spins. It never lands. It floats in the air, humming softly.")
    print("Light and shadow twist around you, pulling you into the coin’s reflection.")
    print("You fall through your own greed, into a city made of mirrors and screams.")
    print()
    print("No one ever sees you again — but sometimes, when a coin is flipped, your reflection appears for a moment, grinning.")
    print()
    print("=== ENDING: THE COIN’S CURSE ===")
    print("Fate does not forgive. It only collects interest.")
    print()
    print("1. Restart")
    print("2. Exit")
    choice = input("> ")
    if choice == "1":
        start_fantasy()
    elif choice == "2":
        exit()
    else:
        fate_coin_flip()




def beggar_belongings():
    while True:
        print("The things you gotten after stealing from the beggar are: Fire scroll, Teleport scroll, Dagger")
        print("1. Use coin")
        print("2. Use coin")
        print("3. Use coin")
        choice = input("> ")
        if choice == "1":
            print("The coin start levitating towards the items")
        elif choice == "2":
            print("The coin starts glowing")
        elif choice == "3":
            Coininium()
            break
        else:
            print("Invalid. Try again")
            beggar_belongings()

def Coininium():
    print("The items combine to make a Quarter. This Quarter can grant you any wish you want. What will you wish for?")
    print("1. Return me to my original world")
    print("2. Grant me unlimited power")
    print("3. A sandwich")
    print("4. Break the Quarter")
    choice = input("> ")
    if choice == "1":
        coin_return()
    elif choice == "2":
        unlimited_death()
    elif choice == "3":
        sandwich()
    elif choice == "4":
        end()
    else:
        print("Invalid. Try again")
        Coininium()

def coin_return():
    print("COIN RETURN. You wish to go back to your original world. You return a day hasn't passed. You didn't make that many sacrifices lucky you")

def unlimited_death():
    print("DIVINE INTERVENTION ENDING. You wish for unlimited power. Little did you know you can't wish that their is a higher being from preventing you from doing that. No shortcuts. You get atomized.")

def sandwich():
    print("SANDWICH ENDING. You get a sandwich")

def end():
    print("END OF THE WORLD. You break the coin. The ground begins to shake, the sun explodes, everything goes white.")






def sin_achieved():
    print("The beggars head was split open you take the cup of money he had on the ground and walk away. You feel stronger.")
    print("Tails")
    print("Heads")
    choice = input("> ")
    if choice == "1":
        tails_riot()
    elif choice == "2":
        misguided_heads()
    else:
        print("Invalid. Try again?")
        sin_achieved()


def misguided_heads():
    print("THE FREAK ENDING. You get heads and have a nicer approach to things but people can see death in your eyes your actions are nice but not genuine. A monster.")








def tails_riot():
    print("Tails. Tails. Tails. You used the money to cause a riot inside of the town.")
    print("1. Sin")
    choice = input("> ")
    if choice == "1":
        tails_mad()
    else:
        print("Invalid. Try again")
        tails_riot()

def tails_mad():
    print("THE SINNER ENDING. You became a chaotic but not a powerful one and conniving one that enjoys the suffering of others. With the coin in your hand ready to flip for the choice of mayhem thats in store for anyone in your path")





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
    print("ADVENTURER ENDING. You gained enough orderly to teleport back to your world")







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

def inevitable_sloth():
    print("You run away from the cloaked man. A lot has happened all at once first you need shelter.")
    print("1. Go to a cave.")
    print("2. See if you can get some money for an inn.")
    choice = input("> ")
    if choice == "1":
        cave()
    elif choice == "2":
        inn()
    
    else:
        print("Invalid. Try again")
        inevitable_sloth()


def cave():
    print("You find a cave and seek refuge there. You gained some chaotic from those bandits and can experiment with it. What will you do?")
    print("1. Experiment with your chaotic to see what you can do")
    print("2. Choose not to")
    choice = input("> ")
    if choice == "1":
        cave_chaotic()
    elif choice == "2":
        cave_not()
    else:
        print("Invalid. Try again")
        cave()









def inn():
    print("You decided for the inn option. How will you gain money?")
    print("Employment")
    print("Nah Imma do my own thing")
    choice = input("> ")
    if choice == "1":
        inn_employment()
    elif choice == "2":
        rob_someone()
    else:
        print("Invalid. Try again")
        inn()


def rob_someone():
    print("You rob someone and gain money to buy a room in the inn")
    print("You settle down their for a while in till your out of money again. What will you do")
    print("1. Rob someone")
    choice = input("> ")
    if choice == "1":
        rob_someone2()
    else:
        print("Invalid. Try again")
        rob_someone()

def rob_someone2():
    print("ROBBER ENDING. You kept on robbing people in till you gained a reputation for yourself. People call you the robber. They say that if you stay past midnight the robber will rob you")



def inn_employment():
    print("You decided to work for the inn this way you can live at the inn while also gaining money")
    print("You work their for a couple weeks in till you get caught for murdering 3 people")
    print("The police raid you. You have to do something!")
    print("1. Fight back")
    print("2. Run away")
    choice = input("> ")
    if choice == "1":
        police_route()
    elif choice == "2":
        caught_police()
    else:
        print("Invalid. Try again")
        inn_employment()





def caught_police():
    print("RUN AWAY ENDING. You ran and you ran in till you couldn't anymore. You're forever wanted and can't settle down. You decide to just end it all")




def police_route():
    print("POLICE ENDING. You fight back valiantly and the chief of the police sees this and sees the skills you have. You get recruited to the police and work for them now")
    







def cave_not():
    print("CAVE RAIDED. You chose not to experiment with your chaotic which made you inexperienced in fights of orderly and chaotic eventually getting your cave raided and dying trying to defend it.")






def cave_chaotic():
    print("You experimented with your chaotic and figured out you can infuse your will onto to object and others. This power seems corrupted to a extent but can also make you powerful. What will you chose ")
    print("1. Temperance")
    print("2. Over-indulgence")
    choice = input("> ")
    if choice == "1":
        cave_dweller()
    elif choice == "2":
        chaotic_demon()
    else:
        print("Invalid. Try again")    
        cave_chaotic()


def chaotic_demon():
    print("CHAOTIC DEMON ENDING. You chose to gain more chaotic but instead of ascending you became known as a chaotic demon. A person who doesn't ascend stays stagnant in till they evolve into something more gruesome")



def cave_dweller():
    print("CAVE DWELLER ENDING. You chose not to gain more chaotic. You decided to make the cave your home since you were wanted for 3 murders. You became strong enough to defend yourself well so you lived a long life.")



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


def wrath_if():
    print("You decide to recruit the bandits. They could be helpful but first the woman. What will you do?")
    print("1. ...")
    print("2. Spare her")
    choice = input("> ")
    if choice == "2":
        wrath_spare()
    elif choice == "1":
        wrath_sin()
    else:
        print("Invalid. Try again")
        wrath_if()





def wrath_sin():
    print("You walk out of the alley and hear some noises you chose to ignore that doesn't matter anymore. You have to recruit others to acheive your goal")
    print("You see a weird coin on the ground. Will you pick it up?")
    print("1. Pick it up")
    print("2. Don't pick it up")
    choice = input("> ")
    if choice == "1":
        wrath_definite()
    elif choice == "2":
        wrathit()
    else:
        print("Invalid. Try again")
        wrath_sin()



def wrathit():
    print("You decide not to pick it up. You have work to do but you feel to untrusty to the point you decide not to recruit anyone else.")
    print("You felt a bit more powerful after you left the alleyway so you decide that how you will complete your goal.")
    print("1. Call the bandits over to you and ....")
    choice = input("> ")
    if choice == "1":
        pending_wrath()
    else:
        print("Invalid. Try again")
        wrathit()



def pending_wrath():
    print("You gained some chaotic off those people. A scaredy cat betraying and hiding away from people. How dissapointing.")
    print("1. Wander")
    choice = input("> ")
    if choice == "1":
        wanderer_ending()
    else:
        print("Invalid. Try again")
        pending_wrath()

def wanderer_ending():
    print("WANDERER ENDING. You wander the vast plains asking people for help little do they know you are a chaotic....")
    


def wrath_definite():
    print("You picked up the coin and you felt the coins influence fully control you.")
    print("You suddenly felt very paranoid you need trust worthy people around you.")
    print("1. Imbue chaotic into the coin and flip it.")
    choice = input("> ")
    if choice == "1":
        wrath_king()
    else:
        print("Invalid. Try again.")
        wrath_definite()

def wrath_king():
    print("You gained glimpses of people you need to recruit in your mind. You tell your subordinates to recruit these specific people.")
    print("You hear rumours of a mysterious scroll that can teleport people. You decide to do the most effecient route you know")
    print("1. Wrath.")
    choice = input("> ")
    if choice == "1":
        wrath_ending()
    else:
        print("Invalid. Try again.")
        wrath_king()

def wrath_ending():
    print("WRATH ENDING. You monopolize the underground market in order for the scroll to circulate to you. You aren't very trusting towards any of your subordinates so you decide if they should die or not. The scroll never gets to you so now you sit their paranoid of the people around you and the people being afraid of you with the reputation of The King of Eradication")





def wrath_spare():
    print("I don't need her anyway. You tell the bandits to gather information around town. You need to start recruiting people in order to acheive my goal.")
    print("The group comes back and tells you about a mysterious scroll going around the merchant system said to be able to teleport people and things")
    print("What will you do in order to achieve this scroll?")
    print("1. Monopoly the merchant market")
    print("2. Recruit more people")
    choice = input("> ")
    if choice == "2":
        wrath_betrayal()
    elif choice == "1":
        wrath_merchants()
    else:
        print("Invalid. Try again")
        wrath_spare()


def wrath_merchants():
    print("MONOPOLIZATION ENDING. You recruited all the active merchants in the market and becamt dominant in the market. The scroll circulated to you and you used it to return to your original world")



def wrath_betrayal():
    print("BETRAYAL ENDING. You ended up recruiting more people but the people you recruited weren't that trut worthy and took your life for the info you had")



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