import random
from itertools import combinations

nums = [random.randint(1, 15) for _ in range(20)]
print(nums)

for r in range(2, len(nums) + 1):
    for combo in combinations(nums, r):
        if 30 <= sum(combo) <= 32:
            print(combo)
print("*****************************")            
print(nums)
print("*****************************") 