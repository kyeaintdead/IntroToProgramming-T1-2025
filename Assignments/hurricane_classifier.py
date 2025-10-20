hurricane = int(input("Give me the wind speed in MPH\n>"))
if hurricane < 74:
    print("Tropical storm")
elif hurricane < 96:
    print("Category 1")
elif hurricane < 111:
    print("Category 2")
elif hurricane < 130:
    print("Category 3")
elif hurricane < 157:
    print("Category 4")
elif hurricane >= 157:
    print("Category 5")

