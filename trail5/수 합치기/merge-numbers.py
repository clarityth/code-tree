n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
from heapq import heappush, heappop, heapify

ans = 0

heapify(arr)
while arr and len(arr) > 1:
    first = heappop(arr)
    second = heappop(arr)
    ans += first+second
    heappush(arr, (first+second))

print(ans)