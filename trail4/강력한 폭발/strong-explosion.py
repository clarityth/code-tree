n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
vertical = [(-1, 0), (-2, 0), (1, 0), (2, 0)]
plus = [(0, -1), (0, 1), (-1, 0), (1, 0)]
x = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
patterns = [vertical, plus, x]

ans = 0
bombs = []
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            bombs.append((row, col))
b_len = len(bombs)

def dfs(depth, visited):
    global n, bombs, b_len, ans
    if depth == b_len:
        ans = max(ans, len(set(visited)))
        return
    
    cur_row, cur_col = bombs[depth][0], bombs[depth][1]
    visited.append((cur_row, cur_col))
    
    for i in range(len(patterns)):
        appended_cnt = 0
        for j in range(4):
            next_row = cur_row+patterns[i][j][0]
            next_col = cur_col+patterns[i][j][1]
            if 0 <= next_row < n and 0 <= next_col < n:
                visited.append((next_row, next_col))
                appended_cnt += 1
        dfs(depth+1, visited)
        for i in range(appended_cnt):
            visited.pop()

    visited.pop()

dfs(0, [])
print(ans)