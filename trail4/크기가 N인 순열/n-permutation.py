n = int(input())

# Please write your code here.
from itertools import permutations
for perm in permutations(range(1, n+1)):
    print(*perm)