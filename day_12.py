# Day 12: Sets and Set Operations

# Union function
def union(set1, set2):
    set_union = set1.copy()
    for item in set2:
        if item not in set_union:
            set_union.add(item)
    return set_union

# Intersection function
def intersection(set1, set2):
    set_intersect = set()
    for item in set1:
        if item in set2:
            set_intersect.add(item)
    return set_intersect

# Multiple sets intersection function
def intersection_mult(*mult_sets):
    if len(mult_sets) > 1 and len(mult_sets[0]) > 0:
        set_intersect = mult_sets[0].copy()
        for item in mult_sets[0]:
            for set_ in mult_sets[1:]:
                if item not in set_:
                    set_intersect.remove(item)
        return set_intersect
    return set()

# Difference function
def difference(set1, set2):
    set_difference = set()
    for item in set1:
        if item not in set2:
            set_difference.add(item)
    return set_difference

# Sample Space function using union of multiple sets
def union_mult_sets(*mult_sets):
    sample_space = set()
    for set_ in mult_sets:
        sample_space = union(sample_space, set_)
    return sample_space

# Complement function using difference between sample space and set1
def complement(sample_space, set1):
    return difference(sample_space, set1)

# Test sets for set operations
a = {'bat', 'cat', 'dog', 'porpoise', 'whale', 'ant', 'bear'}
b = {'bat', 'cat', 'dog', 'eagle', 'shark', 'anteater', 'gull'}
c = {'porpoise', 'platypus', 'crane', 'hermit crab', 'shark', 'anteater', 'gull'}

# Testing union function
print("Union:", union(union(a, b), c))

# Testing intersection function
print("Intersection:", intersection(a, b)) # Output: {'bat', 'cat', 'dog'}

# Testing multiple sets intersection function
print("Multiple Sets Intersection:", intersection_mult(a, b, c))

# Testing difference function
print("Difference:", difference(a, b))

# Testing sample space using union of multiple sets
sample_space = union_mult_sets(a, b, c, {'elephant', 'hippo', 'nutria'})
print("Sample Space:", sample_space)

# Testing complement function
print("Complement:", complement(sample_space, a))


# Testing set properties
set1 = {'a', 'b', 'c'}
set2 = {'c', 'd', 'e'}
set3 = {'a', 'e', 'f'}

# Testing commutative property
print(set1.union(set2) == set2.union(set1))
print(set1.intersection(set2) == set2.intersection(set1))

# Testing associative property
a = True
b = False
c = True
print((a or b) == (b or a))
print((a and b) == (b and a))
print(set1.union(set2).union(set3) == set3.union(set2).union(set1))
print(set1.intersection(set2).intersection(set3) == set3.intersection(set2).intersection(set1))
print(((a or b) or c) == (a or (b or c)))
print(((a and b) and c) == (a and (b and c)))
