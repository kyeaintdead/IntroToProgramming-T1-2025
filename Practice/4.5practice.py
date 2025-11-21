# Example of a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 25
print(my_dict.get("country", "Not Found"))  # Output: Not Found

# Adding a new entry
my_dict["country"] = "USA"

# Modifying an existing entry
my_dict["age"] = 26

print(my_dict)

# Removing an entry
del my_dict["city"]  # Removes the key "city"

age = my_dict.pop("age")  # Removes the key "age" and returns its value

print(my_dict)  # Output: {'name': 'Alice', 'country': 'USA'}
print(age)  # Output: 26

# Looping through keys
for key in my_dict:
    print(key)

# Looping through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
#- `my_dict.keys()` - Returns a view object displaying a list of all the keys.
#- `my_dict.values()` - Returns a view object displaying a list of all the values.
#- `my_dict.items()` - Returns a view object displaying a list of key-value tuple pairs.
#- `my_dict.clear()` - Removes all items from the dictionary.


# Example of using dictionary methods
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys)   # Output: dict_keys(['name', 'country'])
print(values) # Output: dict_values(['Alice', 'USA'])
print(items)  # Output: dict_items([('name', 'Alice'), ('country', 'USA')])

