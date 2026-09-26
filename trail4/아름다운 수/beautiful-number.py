n = int(input())

# Please write your code here.
ans = 0
def dfs(length):
    global ans
    if length == n:
        ans += 1
        return 
    
    if length > n:
        return

    for i in range(1, 5):
        dfs(length+i)

dfs(0)
print(ans)