#question = input("What comes first the chicken or the egg\n>")
#question = int(input("Give me a number less than 10 less than 30\n>"))
#question = input("Which one comes first Milk or Cereal\n>")
#question = input("What School are you from\n>")
#question = input("What is the sum of 2 + 2\n>")

a = 0 
b = 11 
c = 52 
#if True:
    #print("if statement ran") #if True: if statement gets printed but else doesnt because if worked
#else:
    #print("plum") # we get plum because the if statement failed 


def again():
  password = "123"
  password = input("What is the password")
  
  if password == "123":
    print("You got it")
  else:
    print("Try again")
    again()
again()