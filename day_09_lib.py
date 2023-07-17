# Function using a while loop to find divisors of a positive number
def divisors_list_while(n):
    lst = []
    i = 1
    while i <= n:
        if n % i == 0:
            lst.append(i)
        i += 1
    return lst

# Function using a for loop to find divisors of a positive number
def divisors_list_for(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst

# Test the functions for numbers from 0 to 19
for i in range(20):
    print(i, divisors_list_while(i))
    print(i, divisors_list_for(i))
