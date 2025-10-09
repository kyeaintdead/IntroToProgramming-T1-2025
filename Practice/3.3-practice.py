#str.upper() capitalize all charcter 
#str.lower() lowercase all characters 

sentence = input("Give me a sentence\n>")
print(sentence.upper())
print(sentence.strip())
print(sentence.replace("bad" , "good"))

if sentence.endwith("."):
    print(True)
else:
    print(False)

