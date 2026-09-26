K, N = map(int, input().split())

# Please write your code here.

def dfs(depth, record):
    global K, N
    if depth == N:
        print(*record)
        return

    for i in range(1, K+1):
        record.append(i)
        dfs(depth+1, record)
        record.pop()

dfs(0, [])