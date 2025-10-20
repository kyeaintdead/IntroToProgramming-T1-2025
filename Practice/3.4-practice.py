def times_two():

    num = input("Enter a number\n>")
    try:
     print(int(num) * 2)

    except:
        print("You must enter an interger")
times_two()