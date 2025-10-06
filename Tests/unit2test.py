statement1 = input("Give me the first word \n>")
statement2 = input("Give me the second word \n>")
statement3 = input("Give me the third word \n>")
print("first word " +  statement1  + " second word " + statement2 + " third word " + statement3)


num1 = int(input("Give me a interger\n>"))
num2 = int(input("Give me another interger\n>"))
num3 = int(input("Give me the final interger\n>"))


def add_three(num1, num2,num3):
    print(num1 + num2 + num3)
    add_three(int(num1), int(num2), int(num3))