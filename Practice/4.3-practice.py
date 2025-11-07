#while condition:
# do something

num = 0
continue_adding = True

while continue_adding == True:
    num += 1
    print(num)
    ask = input("Would you like to continue? Y/N \n>")
    if ask.lower() == "n":
        continue_adding = False
