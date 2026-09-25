n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
from heapq import heappush, heappop
from collections import defaultdict
p_dict = defaultdict(int)
for p in price:
    p_dict[p] += 1

pq = []
for p in price:
    heappush(pq, (-p))

max_profit = 0

for p in price:
    p_dict[p] -= 1

    while pq and p_dict[-pq[0]] <= 0:
        heappop(pq)

    if pq:
        max_price = -pq[0]
        profit = max_price - p
        max_profit = max(max_profit, profit)

    else:
        break

print(max_profit)