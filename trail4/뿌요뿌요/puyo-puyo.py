n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
visited = set()
exploded = 0
max_size = 0

def dfs(r, c, val, cnt, record):
    global visited, n, grid
    visited.add((r, c))

    for (dr, dc) in dirs:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == val:
            record.append((nr, nc))
            dfs(nr, nc, val, cnt+1, record)

for r in range(n):
    for c in range(n):
        if (r, c) not in visited:
            record = [(r, c)]
            dfs(r, c, grid[r][c], 1, record)

            max_size = max(max_size, len(record))
            
            if len(record) >= 4:
                exploded += 1
                for del_r, del_c in record:
                    grid[del_r][del_c] = 0

print(exploded, max_size)