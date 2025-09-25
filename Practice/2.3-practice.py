# +- Operations
# defining a value variable = value 
lowercase = False
UPPERCASE = False
UpperCamelCase = False #lowercase,no spaces, capital for new words 
lowerCamelCase = False #lowercase,no spaces, capital for new words 
snake_case = True #All lowercase,underscores for spaces 
SCREAMING_SNAKE_CASE = False

# Other general rules to naming things 
#1. Concise 
the_font_size_for_paragraph = 10 #bad one
font_size_para = 10 #Good one 

# get the number as a string 
num = input("What number do you want to square\n> ")

#Parse (Convert} the string to an interger cast, int converts string to itnerger, float, boolean, str also work
num = int(num)

#do math and print
print(num * num)