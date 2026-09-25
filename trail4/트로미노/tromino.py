n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

from collections import deque
q = deque([])
for i in range(n):
    for j in range(m):
        q.append((i, j, 0, set([(i, j)]), grid[i][j]))

while q:
    cur_row, cur_col, steps, visited, total = q.popleft()

    if steps == 2:
        ans = max(ans, total)
        continue

    for i in range(4):
        next_row, next_col = cur_row+dirs[i][0], cur_col+dirs[i][1]
        if 0 <= next_row < n and 0 <= next_col < m:
            if (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                q.append((next_row, next_col, steps+1, visited, total+grid[next_row][next_col]))

print(ans)
