# Function to generate all possible outcomes of four coin flips (H for heads, T for tails)
def four_flip_sample_space():
    flips = ['H', 'T']
    outcomes = []
    for flip1 in flips:
        for flip2 in flips:
            for flip3 in flips:
                for flip4 in flips:
                    outcomes.append([flip1, flip2, flip3, flip4])
    return outcomes

# Print all possible outcomes of four coin flips
outcomes = four_flip_sample_space()
for outcome in outcomes:
    print(outcome)

# Function to compute the factorial of a positive integer using a for loop
def facty_the_factorial_function(n):
    total = 1
    for num in range(1, n + 1):
        total *= num
    return total

# Test the factorial function with n = 5
print(facty_the_factorial_function(5))  # 120

# Function to compute the factorial of a positive integer using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
