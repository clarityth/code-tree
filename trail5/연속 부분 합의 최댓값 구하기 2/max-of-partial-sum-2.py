n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
ans = -float('inf')

temp = 0
for i in range(n):
    temp += a[i]
    ans = max(ans, temp)

    if temp < 0:
        temp = 0

print(ans)