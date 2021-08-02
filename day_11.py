"""un/comment to de/activate ###########################
​
print({"a": 10, "b": 20} == {"b": 20, "a": 10})
​
#######################################################"""
"""un/comment to de/activate ###########################
​
car = {}
car["make"]  = "toyota"
car["model"] = "highlander"
car["year"]  = 2011
car["color"] = "black"
car["year"] = 2014
​
# print(car)
# print(car["year"])
# for k, v in car.items():
#     print(f"{k} {v}")
​
print( "make", "make" in car        ) # these lines are EXACTLY the same
print( "make", "make" in car.keys() ) # these lines are EXACTLY the same
print( "engine size", "engine size" in car.keys() )
print( "make", "make" in car.values() )
print( "toyota", "toyota" in car.values() )
​
#######################################################"""
"""un/comment to de/activate ###########################
# d.pop(key)
​
car = {
    "make"  : "toyota",
    "model" : "highlander",
    "year"  : 2011,
    "color" : "black",
}
​
print( car )
key = "model"
res = car.pop(key)
print( res )
print( car )
​
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# del
car = {
    "make"  : "toyota",
    "model" : "highlander",
    "year"  : 2011,
    "color" : "black",
}
​
print( car )
key = "model"
del car[key]
print( car )
​
#######################################################"""
"""un/comment to de/activate ###########################
​
def find_thing(d, thing_to_find, alt=None):
    if state in d.keys():
        return d[thing_to_find]
    else:
        return alt
​
​
d = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}
​
state = "Colorado"
print( find_thing(d, state, "state not found") )
print( d.get(state, "state not found") )
​
state = "Washington"
print( find_thing(d, state, "state not found") )
​
print( d.get(state, len(state)) )
print( d.get(state) )
​
# d.get('Washington', 'Capital not found')
​
#######################################################"""
"""un/comment to de/activate ###########################
​
car1 = {
    "make"  : "toyota",
    "model" : "highlander",
    "year"  : 2011,
    "color" : "black",
}
​
car2 = car1.copy() # this is a "deep" copy
del car2["color"]
del car1["make"]
print(car1)
print(car2)
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# positive
def positive_make_standard_car(d_in):
    d = {}
    for k, v in d_in.items():
        if k in ["make", "model", "year"]:
            d[k] = v
​
    return d
​
​
car = {
    "make"  : "toyota",
    "model" : "highlander",
    "year"  : 2011,
    "color" : "black",
}
​
print( positive_make_standard_car(car) )
print( car )
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# negative
def negative_make_standard_car(d_in):
    d = d_in.copy()
    for k, v in d_in.items():
        if k not in ("make", "model", "year"):
            del d[k]
​
    return d
​
​
car = {
    "make"  : "toyota",
    "model" : "highlander",
    "year"  : 2011,
    "color" : "black",
}
​
print( negative_make_standard_car(car) )
print( car )
​
#######################################################"""
"""un/comment to de/activate ###########################
​
# types
    # int, float
    # bool
    # None
    # str
    # *tuple
​
    # list
    # dict
    # set
​
#######################################################"""
"""un/comment to de/activate ###########################
​
my_set = set([4, 5, 3, 3])
print( my_set )
my_set = set("hello world")
print( my_set )
my_set = set(["hello", "hello", "world"])
print( my_set )
​
#######################################################"""
"""un/comment to de/activate ###########################
​
set1 = set([4, 5, 2, 6, 7])
set2 = set([0, 9, 2, 8, 7])
print( set1.union(set2) )
print( set2.union(set1) )
​
print( set1.intersection(set2) )
print( set2.intersection(set1) )
​
print( set1 - set2 )
print( set2 - set1 )
print( set1.difference(set2) )
print( set2.difference(set1) )
​
#######################################################"""
"""un/comment to de/activate ###########################
​
def my_function(tup):
    for num in (4, 3, 7, 6, 9, 8, 7, 9, 2,):
        tup = tup + (num**2,)
​
    return tup
​
my_tup = ()
print( my_function(my_tup) )
print(my_tup)
​
#######################################################"""
# """un/comment to de/activate ###########################
​
​
​
#######################################################"""
