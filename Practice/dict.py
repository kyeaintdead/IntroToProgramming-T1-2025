names = {
    "Alice": "F",
    "Bob": "C",
    "Charlie": "B+",
    "David": "D",
    "Eve": "F"
}

student = {
    "name": "Alice",
    "age": 16,
    "grade": "A"
}

print(str(student["name"]) + ", " + str(student["age"]))

student["grade"] = "A+"
print(student)


