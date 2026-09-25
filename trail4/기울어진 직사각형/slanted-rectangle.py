n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for row in range(n):
    for col in range(n):
        for w in range(1, n):
            for h in range(1, n):
                total = 0
                cur_r = row
                cur_c = col
                if 0 <= row-h < n and 0 <= row-h-w < n and 0 <= col+w < n and 0 <= col-h < n:
                    for dr, dc, step in [(-1, 1, w), (-1, -1, h), (1, -1, w), (1, 1, h)]:
                        for _ in range(step):
                            cur_r += dr
                            cur_c += dc
                            total += grid[cur_r][cur_c]

                    ans = max(total, ans)

print(ans)