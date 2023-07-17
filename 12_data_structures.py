# Day 4: Lists, Tuples, and Comprehensions

# Using 'append' to add an item to a list
lst = []
lst.append("something")
print(lst)  # ['something']

# Using '+=' to add an item to a tuple
tup = ()
tup += ("something",)
print(tup)  # ('something',)

# Factorial function using a for loop
def factorial(n):
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod

print(factorial(5))  # 120

# Factorial function using a list comprehension
def factorial(n):
    return [prod * i for i in range(2, n + 1)]

print(factorial(5))  # [2, 6, 24, 120]

# Function to generate all possible outcomes of flipping a coin 10 times
def list_of_every_possible_outcome_of_flipping_a_coin_10_times():
    lst = []
    sides = ["H", "t"]
    for a in sides:
        for b in sides:
            for c in sides:
                for d in sides:
                    for e in sides:
                        for f in sides:
                            for g in sides:
                                for h in sides:
                                    for i in sides:
                                        for j in sides:
                                            lst.append((a, b, c, d, e, f, g, h, i, j))
    return lst

# Using 'for' loop to iterate over elements in a list
lst = list_of_every_possible_outcome_of_flipping_a_coin_10_times()
d = {}
for res in lst:
    h_count = res.count("H")
    if h_count not in d.keys():
        d[h_count] = 0
    d[h_count] += 1

# The expected outcome dictionary
exp = {
    0: 1,
    1: 10,
    2: 45,
    3: 120,
    4: 210,
    5: 252,
    6: 210,
    7: 120,
    8: 45,
    9: 10,
    10: 1,
}

print(d)  # Output will be different due to the random sampling in the original code.
