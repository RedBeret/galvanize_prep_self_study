#def factorial(n):
#    prod = 1
#    for num in range(2, n+1):
#        prod *= num
#    return prod
##print(factorial(5))
#
#def permutations(n, k):
#    return int(factorial(n) / factorial(n-k))
##print(permutations(850, 100))
#def permutations(n, k):
#    perm = 1
#    for i in range(n, n-k, -1):
#        perm *= i
#    return perm
##print(permutations(850, 100))
#
#animals_perms = []
#for an_list in animals_counting:
#    perm = True
#
#    for an in an_list:
#        if an_list.count(an) > 1:
#            perm = False
#            break
#    if perm:
#        animals_perms.append(an_list)
#

#def permutations(n, k):
#    return int(factorial(n) / factorial(n-k))
## print(permutations(850, 100))
#def permutations(n, k):
#    perm = 1
#    for i in range(n, n-k, -1):
#        perm *= i
#    return perm
## print(permutations(850, 100))
#base_5 = ['ant', 'bat', 'crawdad', 'eagle', 'falcon']
#animals_counting = []
#for an1 in base_5:
#    for an2 in base_5:
#        for an3 in base_5:
#            for an4 in base_5:
#                for an5 in base_5:
#                    animals_counting.append([an1, an2, an3, an4, an5])
## for an in animals_counting:
##     print(an)
#animal_perms = []
#for an_list in animals_counting:
#    perm = True
#    for an in an_list:
#        if an_list.count(an) > 1:
#            perm = False
#            break
#    if perm:
#        animal_perms.append(an_list)
# for an_list in animal_perms:
#     print(an_list)

#def swap(lst, idx_1, idx_2):
#    lst_ = lst.copy()
#    temp = lst_[idx_2]
#    lst_[idx_2] = lst_[idx_1]
#    lst_[idx_1] = temp
#    return lst_
#
#test = [1,2,3,4,5]
#print(swap(test, 0, 2))

#def combinations(n, k):
#    return int(factorial(n) / (factorial(n-k)*factorial(k)))
#print(combinations(21, 5))
#def combinations(n, k):
#    perm = 1
#    for i in range(n, n-k, -1):
#        perm *= i
#    return int(perm / factorial(k))
#print(combinations(21, 5))

# an expensive sampling approach
#from random import choice
#def basketball_combs_samp(team_size=11, num_players=5):
#    combs = []
#    player_range = range(1, team_size+1)
#    while len(combs) < combinations(team_size, num_players):
#        player_comb = []
#        while len(player_comb) < num_players:
#            player_num = choice(player_range)
#            if player_num not in player_comb:
#                player_comb.append(player_num)
#        player_comb = sorted(player_comb)
#        if player_comb not in combs:
#            print(player_comb)
#            combs.append(player_comb)
#    return combs
## team_size = 21
# num_players = 5
# print(len(basketball_combs_samp(team_size , num_players)))
# print(combinations(team_size, num_players))



#def combs_from_itertools(lst, k):
#    # get a frozen version of the input
#    lst_frozen = tuple(lst)
#    n = len(lst_frozen)
#    combs = []
#    if k > n: return
#    indices = list(range(k))
#    yield tuple(lst_frozen[i] for i in indices)
#    while True:
#        for i in reversed(range(k)):
#            if indices[i] != i + n - k:
#                break
#        else:
#            return
#        indices[i] += 1
#        for j in range(i+1, k):
#            indices[j] = indices[j-1] + 1
#        yield tuple(lst_frozen[i] for i in indices)
#bask_nums = list(range(1, 21+1))
#counter = 0
#for team in combs_from_itertools(bask_nums, 5):
#    print(team)
#    counter += 1
#print(counter)
#print(combinations(21, 5))