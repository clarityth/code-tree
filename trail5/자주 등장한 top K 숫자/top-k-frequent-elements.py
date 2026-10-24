n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import Counter
cnts = list(Counter(arr).items())
s_cnts = sorted(cnts, key=lambda x: (-x[1], -x[0]))[:k]

for num, _ in s_cnts:
    print(num, end=' ')