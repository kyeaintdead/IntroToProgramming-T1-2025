
answer1 = input("Give me the infamous number\n>")

answer2 = input("Which one comes first Milk or Cereal\n>")


answer3 = input("What School are you from STMA or somewhere else\n>")


answer4 =input("What is the sum of 2 + 2\n>")


answer5 = input("What comes first the chicken or the egg\n>")


def simplequiz():
    score = 0 
   


    if answer4.lower() == "4":   
       score = score + 1
    
       
    if answer1 == "67":
         score = score + 1
    
    

    if answer2.lower() == "cereal":
        score = score + 1
   
    if answer3.lower() == "stma":
        score = score + 1 
    
    if answer5.lower() == "chicken":
         score = score + 1
    
    print("SCORE:  "  + str(score) + "/5")
simplequiz()
