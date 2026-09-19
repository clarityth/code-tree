n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
row_cnt = 0
col_cnt = 0

for row in range(n):
    row_same_cnt = 1
    row_prev = None
    for col in range(n):
        if not row_prev:
            row_prev = grid[row][col]
        else:
            if row_prev == grid[row][col]:
                row_same_cnt += 1
            else:
                row_same_cnt = 1
            row_prev = grid[row][col]
        if row_same_cnt >= m:
            row_cnt += 1
            break

for col in range(n):
    col_same_cnt = 1
    col_prev = None
    for row in range(n):
        if not col_prev:
            col_prev = grid[row][col]
        else:
            if col_prev == grid[row][col]:
                col_same_cnt += 1
            else:
                col_same_cnt = 1
            col_prev = grid[row][col]
        if col_same_cnt >= m:
            col_cnt += 1
            break

print(col_cnt+row_cnt)