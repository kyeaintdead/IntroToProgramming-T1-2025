
answer = input("Give me the infamous number\n>")


answer = input("Which one comes first Milk or Cereal\n>")


answer = input("What School are you from STMA or somewhere else\n>")


answer = input("What is the sum of 2 + 2\n>")


answer = input("What comes first the chicken or the egg\n>")


def simplequiz():
    answer = "67"
    answer = "Cereal"
    answer = "STMA"
    answer = "Nike"
    answer = "chicken"


    if answer == "Nike":
        print("You got it")
    else:
        print("Wrong bozo")
       
    if answer == "67":
         print("You got it")
    else: 
            print("Wrong bozo")
    

    if answer == "Cereal":
        print("You're a normal person good job")
    else:
        print("Wrong try again bozo")
    if answer == "STMA":
        print("You are form stma")
    else:
         print("You are from another school")
    if answer == "chicken":
         print("You got it")
    else:
         print("You got it wrong")
         simplequiz()
simplequiz()