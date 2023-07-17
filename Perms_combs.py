# Day 6: Permutations, Combinations, and Basketball Teams

# Helper function to calculate the factorial of a number
def factorial(n):
    prod = 1
    for num in range(2, n+1):
        prod *= num
    return prod

# Permutations: Function to calculate the number of permutations (nPk)
def permutations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return perm

# Combinations: Function to calculate the number of combinations (nCk)
def combinations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return int(perm / factorial(k))

# Basketball Team Combinations: Expensive sampling approach
from random import choice

def basketball_combs_samp(team_size=11, num_players=5):
    combs = []
    player_range = range(1, team_size+1)
    while len(combs) < combinations(team_size, num_players):
        player_comb = []
        while len(player_comb) < num_players:
            player_num = choice(player_range)
            if player_num not in player_comb:
                player_comb.append(player_num)
        player_comb = sorted(player_comb)
        if player_comb not in combs:
            print(player_comb)
            combs.append(player_comb)
    return combs

# Combinations from itertools: A more efficient approach using itertools.combinations
from itertools import combinations as combs_from_itertools

# Example usage of combs_from_itertools
bask_nums = list(range(1, 21+1))
counter = 0
for team in combs_from_itertools(bask_nums, 5):
    print(team)
    counter += 1
print(counter)
print(combinations(21, 5))
