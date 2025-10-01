def calculate_tax(item, price, rate):
    print("The amount of tax to be collected on a " + str(price) + " dollar " + item + " is " + str((.01*price*rate)))


    calculate_tax("Starbucks", 7.99, 0.6825)