n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
row_cnt = 0
col_cnt = 0

for row in range(n):
    if m == 1:
        row_cnt += 1
        continue

    row_same_cnt = 1
    row_prev = grid[row][0]
    for col in range(1, n):
        if row_prev == grid[row][col]:
            row_same_cnt += 1
        else:
            row_same_cnt = 1
        row_prev = grid[row][col]

        if row_same_cnt >= m:
            row_cnt += 1
            break

for col in range(n):
    if m == 1:
        col_cnt += 1
        continue
        
    col_same_cnt = 1
    col_prev = grid[0][col]
    for row in range(1, n):
        if col_prev == grid[row][col]:
            col_same_cnt += 1
        else:
            col_same_cnt = 1
        col_prev = grid[row][col]

        if col_same_cnt >= m:
            col_cnt += 1
            break

print(col_cnt+row_cnt)