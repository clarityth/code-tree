n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
ans = 0
remain = k
for i in range(n-1, -1, -1):
    ans += remain//coins[i]
    remain = remain % coins[i]

print(ans)