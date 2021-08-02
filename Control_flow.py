#def five_or_three(num):
#    if num == 5 or num == 3:
#        return True
#    return False
#print(five_or_three(3))

########################################################

'''def is_divisible_by(num, divisor1, divisor2):
    if num % divisor1 ==0 and num % divisor2 == 0:
        return f'This number is divisible by {divisor1} and {divisor2}.'
    elif num % divisor1 == 0:
        return f'This number is divisible by {divisor1}.'
    elif num % divisor2 == 0:
        return f'This number is divisible by {divisor2}.'
    else:
        return f'This number is not divisible by either {divisor1} or {divisor2}.'
    
    
 # Prints 'This number is divisible by 3.'
print(is_divisible_by(9, 3, 2))

# Prints 'This number is divisible by 3.'
print(is_divisible_by(12, 5, 3))

# Prints 'This number is divisible by 3 and 4.'
print(is_divisible_by(12, 3, 4))

# Prints 'This number is not divisible by either 5 or 7.'
print(is_divisible_by(12, 5, 7))'''

####################################################

'''def depends_on_the_type(obj):
    if type(obj) == int:
        if obj == 0:
            return 'Zero'
        elif obj % 2 == 0:
            return obj**2
        elif obj % 2 ==1:
            return obj**3
    elif type(obj) == float:
        return obj * 1.5
    elif type(obj) == str:
        return obj + obj
    elif type(obj) == bool:
        return not obj
    else:
        return None

print (depends_on_the_type(0))
print (depends_on_the_type(2))
print (depends_on_the_type(3))
print (depends_on_the_type(0.5))
print (depends_on_the_type('hello'))
print (depends_on_the_type(False))
print (depends_on_the_type(None))'''

#####################################################

'''
# comparing strings
if 5 == 5:
    # This will print `True`
    print("hello there" == "hello there") 

if 5 == 5:
    # This will print `False`
    print("hello" == "hi")
    
# strings can be said to be equal if they contain exactly the same content, as shown above

# comparing numbers
if 5 == 5:
    # This will print `True`
    print(5 == 5) 

if 5 == 5:
    # This will print `False`
    print(5 != 5) '''

#####################################################
'''def is_old_enough_to_drink(age):
    if age > 20:
        return (True)
    else:
        return (False)

output = is_old_enough_to_drink(22)
print(output) # --> True'''
#####################################################

'''
def is_old_enough_to_drive(age):
    if age > 15:
        return (True)
    else:
        return (False)

output = is_old_enough_to_drive(15)
print(output) # --> False
'''

#####################################################
'''
def is_old_enough_to_vote(age):
    if age > 17:
        return (True)
    else:
        return (False)

output = is_old_enough_to_vote(22)
print(output) # --> False'''
####################################################
'''def is_old_enough_to_drink_and_drive(age):
    return (False)
'''
####################################################
'''
def special_or(expression1, expression2):
    if not expression1 == True and not expression2 == True :
        return False
    return True

output = special_or(True, False)
print(output) # --> True
'''
####################################################
'''
def is_either_even_or_are_both_7(num1, num2):
    if num1 % 2 == 0 or num2 % 2 == 0:
        return True
    elif num1 == 7 and num2 == 7:
        return True
    return False
        
output = is_either_even_or_are_both_7(3, 7)
print(output) # --> False

output = is_either_even_or_are_both_7(2, 3)
print(output) # --> True
'''
####################################################
'''
def is_either_even_and_less_than_9(num1, num2):
    if not num1 < 9 or not num2 < 9:
        return False
    elif not num1 % 2 == 0 and not num2 % 2 == 0:
        return False
    return True
        
output = is_either_even_and_less_than_9(2, 4)
print(output) # --> True

output = is_either_even_and_less_than_9(72, 2)
print(output) # --> False
'''