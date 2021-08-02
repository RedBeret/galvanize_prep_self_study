'''
* Write a function that computes and returns a list of all of the divisors of some positive number. Use a while loop. Things to think about:
    * How do you determine if a single number is a divisor of another?
    * What is your stopping condition?
    * BONUS: rewrite this with a for loop

    input: n <int>: a positive integer

    output: <list <int> >: representing all the divisor of n


   def divisors_list(n):
    pass
for i in range(20):
    print(i, divisors_list(i) ) 
'''
'''
def carl_the_divisor_finder(num):
  return_list = []
  for each in range(1, int((num/2)+1)):
    if num % each == 0:
      return_list.append(each)
  return_list.append(num)
  return return_list
print(carl_the_divisor_finder(10)) #[1,2,5,10]
print(carl_the_divisor_finder(15)) #[1,2,5,15]
'''
'''
def divisors_list(n):
    lst = []
    for i in range(n+1):
        if n % i == 0:
            lst.append(i)
    return lst

for i in range(20):
    print(i, divisors_list(i))
'''
