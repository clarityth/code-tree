n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import defaultdict

ans = 0
golds = []
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            golds.append((row, col))

if not golds:
    print(0)
    exit(0)
    
for row in range(n):
    for col in range(n):
        gold_k = defaultdict(int)
        for (gold_row, gold_col) in golds:
            k = abs(gold_row-row)+abs(gold_col-col)
            gold_k[k] += 1

        max_k = max(gold_k.keys())
        cum_sum = 0
        for k in range(max_k+1):
            cost = k*k+(k+1)*(k+1)
            cum_sum += gold_k[k]
            if cum_sum*m >= cost:
                ans = max(ans, cum_sum)

print(ans)
