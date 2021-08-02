##append
#lst = []
#lst.append("something")
#print(lst)
#
#tup = ()
#tup += ("something",)
#print(tup)
#
##index'
#

#def factorial(n):
#    prod = 1
#    for i in range(2 ,n+1):
#        # iteration: 2
#        # prod = 2
#        # i = 3
#        prod = prod * i
#    return prod
#print(factorial(5))
#
#def factorial(n):
#    p = 1
#    return ([p * i for i in range(2 ,n+1)])
#    
#print(factorial(5))

#def list_of_every_possible_outcome_of_flipping_a_coin_10_times():
#    lst = []
#    sides = ["H" , "t"]
#    for a in sides:
#        for b in sides:
#            for c in sides:
#                lst.append((a,b,c))
#    return lst
#print(list_of_every_possible_outcome_of_flipping_a_coin_10_times())
#
#

"""un/comment to de/activate ###########################
​
# tuples
# review sets
# review dicts
# comprehensions
​
#######################################################"""
"""un/comment to de/activate ###########################
​
lst = [44, 55, 66, 77, 88, 99]
print( lst[2] )
​
tup = (44, 55, 66, 77, 88, 99)
print( tup[2] )
​
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# list methods
# 'append'
    # mutable
# 'clear'
    # mutable
# 'copy'
    # imutable
# 'count'
    # imutable
# 'extend'
    # mutable
# 'index'
    # imutable
# 'insert'
    # mutable
# 'pop'
    # mutable
# 'remove'
    # mutable
# 'reverse'
    # mutable
# 'sort'
    # mutable
​
# item assaignment is a mutable operation
lst = [33, 44, 55]
print(lst)
lst[1] = "hello"
print(lst)
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# 'count'   # imutable
# 'index'   # imutable
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# 'append'
lst = []
# print(id(lst), lst)
lst.append("something")
# print(id(lst), lst)
​
tup = ()
# print(id(tup), tup)
tup += ("something",)
# print(id(tup), tup)
# tup  = tup + ("something",)
​
# 'clear'
# print(tup)
tup = ()
​
# 'copy'
# 'count'
tup = (22, 55, 22, 77, 33, 22, 77, 44)
# print(tup.count(99))
# print(tup.count(55))
# print(tup.count(22))
# print(tup.count(77))
​
# 'extend'
tup = ()
# print(id(tup), tup)
tup += ("something","hello")
# print(id(tup), tup)
​
# 'index'
tup = (22, 55, 22, 77, 33, 22, 77, 44)
# print(tup.index(77))
​
# 'insert'
tup = (22, 55, 22, 77, 33, 22, 77, 44)
exp = (22, 55, 22, 77, "hello", 33, 22, 77, 44)
tup = tup[:4] + ("hello",) + tup[4:]
# print(tup)
​
# 'pop'
tup = (22, 55, 22, 77, 33, 22, 77, 44)
exp = (22, 55, 22, 77, 22, 77, 44)
idx = 4
tup = tup[:idx] + tup[idx+1:]
# print(tup)
​
# 'remove'
tup = (22, 55, 22, 77, 33, 22, 77, 44)
exp = (22, 55, 22, 77, 22, 77, 44)
ele = 33
idx = tup.index(ele)
tup = tup[:idx] + tup[idx+1:]
# print(tup)
​
# 'reverse'
# 'sort'
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# single element tuples
thing1 = ("something",)
thing2 = ("something")
print( type(thing1) )
print( type(thing2) )
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# union
# intersection
# difference # complement
​
#######################################################"""
"""un/comment to de/activate ###########################
​
d = {}
print(id(d), d)
d["key1"] = "value1" # <------
d.update( {"key2": "value2"} )
print(id(d), d)
​
#######################################################"""
"""un/comment to de/activate ###########################
​
car = {
    "make": "toyota" ,
    "modle": "highlander" ,
    "year": "2014" ,
}
​
# print(car)
# print(car)
# print(car)
​
for k, v in car.items():
    print(k, v)
​
# print({"a": 4} + {"b": 5}) #
​
#######################################################"""
"""un/comment to de/activate ###########################
​
["H", "t", "t", "t", "t", "t", "t", "t", "t", "t"]
["t", "H", "t", "t", "t", "t", "t", "t", "t", "t"]
["t", "t", "H", "t", "t", "t", "t", "t", "t", "t"]
["t", "t", "t", "H", "t", "t", "t", "t", "t", "t"]
["t", "t", "t", "t", "H", "t", "t", "t", "t", "t"]
["t", "t", "t", "t", "t", "H", "t", "t", "t", "t"]
["t", "t", "t", "t", "t", "t", "H", "t", "t", "t"]
["t", "t", "t", "t", "t", "t", "t", "H", "t", "t"]
["t", "t", "t", "t", "t", "t", "t", "t", "H", "t"]
["t", "t", "t", "t", "t", "t", "t", "t", "t", "H"]
​
​
exp = {
    0: 1,
    1: 10,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 10,
    10: 1,
}
​
#######################################################"""
"""un/comment to de/activate ###########################
​
d = {
    0: 1,
    1: 10,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 10,
    10: 1,
}
​
# pritn("hello" in d)
print("hello" in d.keys())  # False
print(7 in d.keys())        # True
print(7 in d.values())      # False
print(12 in d.values())     # False
print(10 in d.values())     # True
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# types
    # int, float
    # bool
    # None
    # tuple
    # str
​
    # list
    # dict
    # set
​
# abstraction
    # var
    # functions
​
# control flow
    # if, elif, else
    # conditions
    # bool
​
# iteration
    # comprehensions
    # for
    # while
​
#######################################################"""
"""un/comment to de/activate ###########################
​
src = [ 4, 7, 6, 8, 2, 9 ]
acc = []
for num in src:
    acc.append(num**2)
​
src = [ 4, 7, 6, 8, 2, 9 ]
acc = [ num**2 for num in src ]
​
print(acc)
​
#######################################################"""
"""un/comment to de/activate ###########################
​
src = [ 4, 7, 6, 8, 2, 9 ]
acc = []
for num in src:
    if num < 5:
        acc.append(num**2)
    else:
        acc.append(num**(1/2))
​
​
print(acc)
​
​
src = [ 4, 7, 6, 8, 2, 9 ]
acc = [ num**2 if num < 5 else numA**(1/2) for num in src ]
​
print(acc)
​
#######################################################"""
"""un/comment to de/activate ###########################
​
def factorial(n):
    prod = 1
    return sum([ prod = prod * i for i in range(2, n+1) ])
​
​
print( factorial(5) )
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# counting approach
​
def list_of_every_possible_outcome_of_flipping_a_coin_10_times():
    lst = []
    sides = ["t", "H"]
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
​
​
lst = list_of_every_possible_outcome_of_flipping_a_coin_10_times()
d = {}
for res in lst:
    h_count = res.count("H")
    if h_count not in d.keys():
        d[ h_count ] = 0
    d[ h_count ] += 1
​
​
# print(d) # see below
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
​
#######################################################"""
## """un/comment to de/activate ###########################
## random sampling approach
#​
#import random
#​
#def list_of_flipings(n, m):
#    flip = ["t", "H"]
#    lst = []
#    for _ in range(m):
#        outcome = []
#        for _ in range(n):
#            outcome.append(random.choice(flip))
#        lst.append(outcome)
#​
#    return lst
#​
#​
#lst = list_of_flipings(10, 1024)
#d = {
#    0: 0,
#    1: 0,
#    2: 0,
#    3: 0,
#    4: 0,
#    5: 0,
#    6: 0,
#    7: 0,
#    8: 0,
#    9: 0,
#    10:0,
#}
#​
#for res in lst:
#    d[ res.count("H") ] += 1
#​
#​
#for k, v in d.items():
#    print(k, "*" * int(v**(1/2)) )
#​
#exp = {
#    0: 1,
#    1: 10,
#    2: 45,
#    3: 120,
#    4: 210,
#    5: 252,
#    6: 210,
#    7: 120,
#    8: 45,
#    9: 10,
#    10: 1,
#}
#​
## actual results
#{
#    0: 0,
#    1: 5,
#    2: 37,
#    3: 123,
#    4: 189,
#    5: 270,
#    6: 194,
#    7: 138,
#    8: 57,
#    9: 10,
#    10: 1
#}
#​
#{
#    0: 1,
#    1: 10,
#    2: 50,
#    3: 133,
#    4: 202,
#    5: 264,
#    6: 179,
#    7: 123,
#    8: 48,
#    9: 11,
#    10: 3
#}
#​
#{
#    0: 1,
#    1: 7,
#    2: 47,
#    3: 138,
#    4: 202,
#    5: 241,
#    6: 222,
#    7: 114,
#    8: 40,
#    9: 9,
#    10: 3
#}
#​
########################################################"""
## """un/comment to de/activate ###########################
#​
#​
#​
########################################################"""