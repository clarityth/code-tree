n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for r in range(n-2):
    for c in range(n-2):
        temp = 0
        for dr in range(3):
            for dc in range(3):
                if grid[r+dr][c+dc] == 1:
                    temp += 1

        ans = max(ans, temp)
print(ans)