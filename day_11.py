# Day 11: Dictionaries and Set Operations

# Dictionary examples
# Commented out to avoid redefining the variables when pasting

# Dictionary creation and modification
car = {}
car["make"] = "toyota"
car["model"] = "highlander"
car["year"] = 2011
car["color"] = "black"
car["year"] = 2014  # Modifying the value of an existing key

# Accessing and printing dictionary elements
# for k, v in car.items():
#     print(f"{k}: {v}")

# Check if a key exists in the dictionary
print("make" in car)  # Output: True
print("make" in car.keys())  # Output: True
print("engine size" in car.keys())  # Output: False

# Check if a value exists in the dictionary
print("make" in car.values())  # Output: True
print("toyota" in car.values())  # Output: True

# Removing a key-value pair from the dictionary
# car.pop("model")  # Uncomment to remove the key-value pair

# Using the 'del' keyword to remove a key-value pair
# key = "model"
# del car[key]  # Uncomment to delete the key-value pair

# Function to find a value by key in a dictionary
def find_thing(d, thing_to_find, alt=None):
    if thing_to_find in d.keys():
        return d[thing_to_find]
    else:
        return alt

# Test dictionary
d = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

state = "Colorado"
print(find_thing(d, state, "state not found"))  # Output: Denver
print(d.get(state, "state not found"))  # Output: Denver

state = "Washington"
print(find_thing(d, state, "state not found"))  # Output: state not found
print(d.get(state, len(state)))  # Output: 10 (length of 'Washington')
print(d.get(state))  # Output: None (key not found)

# Deep copy and removing elements from the copy
car1 = {
    "make": "toyota",
    "model": "highlander",
    "year": 2011,
    "color": "black",
}

car2 = car1.copy()  # Creating a deep copy of the dictionary
del car2["color"]
del car1["make"]
print(car1)  # Output: {'model': 'highlander', 'year': 2011}
print(car2)  # Output: {'model': 'highlander', 'year': 2011, 'color': 'black'}

# Positive function to create a new dictionary with specific keys
def positive_make_standard_car(d_in):
    d = {}
    for k, v in d_in.items():
        if k in ["make", "model", "year"]:
            d[k] = v
    return d

# Negative function to remove unwanted keys from the dictionary
def negative_make_standard_car(d_in):
    d = d_in.copy()
    for k, v in d_in.items():
        if k not in ("make", "model", "year"):
            del d[k]
    return d

# Test dictionary for positive and negative functions
car = {
    "make": "toyota",
    "model": "highlander",
    "year": 2011,
    "color": "black",
}

print(positive_make_standard_car(car))  # Output: {'make': 'toyota', 'model': 'highlander', 'year': 2011}
print(car)  # Output: {'make': 'toyota', 'model': 'highlander', 'year': 2011, 'color': 'black'}
print(negative_make_standard_car(car))  # Output: {'make': 'toyota', 'model': 'highlander', 'year': 2011}
print(car)  # Output: {'make': 'toyota', 'model': 'highlander', 'year': 2011, 'color': 'black'}

# Types of data in Python
# int, float, bool, None, str, tuple, list, dict, set

# Example of creating a set and handling duplicates
my_set = set([4, 5, 3, 3])
print(my_set)  # Output: {3, 4, 5}

# Example of creating a set from a string
my_set = set("hello world")
print(my_set)  # Output: {'r', 'e', 'h', ' ', 'w', 'd', 'o', 'l'}

# Example of creating a set from a list with duplicate values
my_set = set(["hello", "hello", "world"])
print(my_set)  # Output: {'world', 'hello'}

# Set operations
set1 = set([4, 5, 2, 6, 7])
set2 = set([0, 9, 2, 8, 7])

print(set1.union(set2))  # Output: {0, 2, 4, 5, 6, 7, 8, 9}
print(set1.intersection(set2))  # Output: {2, 7}
print(set1 - set2)  # Output: {4, 5, 6}
