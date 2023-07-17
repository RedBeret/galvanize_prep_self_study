# Day 5: Comparisons and Conditionals

# Function to check if a number is equal to either 5 or 3
def five_or_three(num):
    return num == 5 or num == 3

print(five_or_three(3))  # True

# Function to check if a number is divisible by the provided divisors
def is_divisible_by(num, divisor1, divisor2):
    if num % divisor1 == 0 and num % divisor2 == 0:
        return f'This number is divisible by {divisor1} and {divisor2}.'
    elif num % divisor1 == 0:
        return f'This number is divisible by {divisor1}.'
    elif num % divisor2 == 0:
        return f'This number is divisible by {divisor2}.'
    else:
        return f'This number is not divisible by either {divisor1} or {divisor2}.'

print(is_divisible_by(9, 3, 2))  # 'This number is divisible by 3.'
print(is_divisible_by(12, 5, 3))  # 'This number is divisible by 3.'
print(is_divisible_by(12, 3, 4))  # 'This number is divisible by 3 and 4.'
print(is_divisible_by(12, 5, 7))  # 'This number is not divisible by either 5 or 7.'

# Function to apply different operations based on the type of input
def depends_on_the_type(obj):
    if type(obj) == int:
        if obj == 0:
            return 'Zero'
        elif obj % 2 == 0:
            return obj**2
        elif obj % 2 == 1:
            return obj**3
    elif type(obj) == float:
        return obj * 1.5
    elif type(obj) == str:
        return obj + obj
    elif type(obj) == bool:
        return not obj
    else:
        return None

print(depends_on_the_type(0))  # 'Zero'
print(depends_on_the_type(2))  # 4
print(depends_on_the_type(3))  # 27
print(depends_on_the_type(0.5))  # 0.75
print(depends_on_the_type('hello'))  # 'hellohello'
print(depends_on_the_type(False))  # True
print(depends_on_the_type(None))  # None
