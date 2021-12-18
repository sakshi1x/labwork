from copy import deepcopy
tup = (1,2,3,[],"a")
print(tup)
tup_clone = deepcopy(tup)
tup_clone[3].append(5)
print(tup_clone)
print(tup)