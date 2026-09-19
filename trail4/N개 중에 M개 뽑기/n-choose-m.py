N, M = map(int, input().split())

# Please write your code here.
from itertools import combinations

for combi in combinations(range(1, N+1), M):
    print(*combi)