#create a function called add_five_numbers that takes five parametsers 
#one for each number
#print the sum of the five numbers
#run the function three times with different arguements 
def add_five_numbers(a,b,c,d,e):
    print("Add" + a + "Plus" + b + "Plus" + c + "Plus" + d + "Plus" + e ) 
    add_five_numbers(10, 20, 30, 40, 50)

    def full_name(first, last):
        print(first + " " + last)
        first_name = input("Your full name is")
    last_name = input("last name")

    def area_calculator(Length, Width):
        print(Length + Width)
        area_calculator(10,20,)
    area_calculator(1,40,)
    area_calculator(50,90,)

def word_smash(a,b):
    print(str(a) + " " + str(b)) 
word_smash("cat", "dog")
word_smash("cat", "dog")
word_smash("cat", "dog")

def echo(a,b):
    print(str(a) + int(b))
    echo("you")