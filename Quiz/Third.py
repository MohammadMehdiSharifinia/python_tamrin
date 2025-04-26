import random

nums = [random.randint(1, 15) for _ in range(20)]

def d(arr, r):
    if r == 0: return [[]]
    if not arr: return []
    return d(arr[1:], r) + [[arr[0]] + x for x in d(arr[1:], r-1)]

for r in range(2, len(nums)+1):
    for c in d(nums, r):
        if 30 <= sum(c) <= 32:
            print(c)

print("*******")
print(nums)
print("*******")
