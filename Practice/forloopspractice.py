numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for num in numbers:
   print(num)
numbers = [3,4,7,3,2,75,33,242,434,100]
total = 0
for num in numbers:
   total += num
print(total)
square_numbers = [1,2,3,4,5]
squared_numbers = []
for num in square_numbers:
    squared_numbers.append(num * num)

print(squared_numbers)

#ask the user to enter a string
#use a for loop to count and print the number of vowels 
num_vowels = 0
my_string = input("Enter a word\n> ")
for car in my_string:
    if car in ["a", "e", "i", "o", "u"]:
        num_vowels += 1

print(num_vowels)


user_num = input("Enter an integer\n>")
try:
    user_num = int(user_num)
except:
    print("Not an integer...")


for i in range(1,10):
    print(str(user_num) + " x " + " = " + str(user_num*i))


names = ["Jon", "Noah", "Ethan", "Owen"]
for name in names:
    print("Hello, " + name + "!")