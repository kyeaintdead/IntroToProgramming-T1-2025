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

studentA = {
    "name": "Bob",
    "age": 17,
    "grade": "C"
}
print(str(studentA["name"]) + ", " + str(studentA["age"]))
print(studentA)

studentC = {
    "name": "Charlie",
    "age": "18",
    "grade": "D-"
}

print(str(studentC["name"]) + ", " + str(studentC["age"]))
print(studentC)

