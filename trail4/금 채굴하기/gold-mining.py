n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

ans = 0
max_k = 2*(n-1)
from collections import deque

for row in range(n):
    for col in range(n):
        visited = set([(row, col)])
        cnt = [0] * (max_k+1)

        q = deque([(row, col, 0)]) 
        while q:
            cur_r, cur_c, cur_step = q.popleft()

            if grid[cur_r][cur_c] == 1:
                cnt[cur_step] += 1

            if cur_step == max_k:
                continue

            for i in range(4):
                next_r, next_c = cur_r+dirs[i][0], cur_c+dirs[i][1]
                if 0 <= next_r < n and 0 <= next_c < n:
                    if (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        q.append((next_r, next_c, cur_step+1))
        
        cum_sum = 0
        for k in range(max_k+1):
            cost = k*k + (k+1)*(k+1)
            cum_sum += cnt[k]
            if cost <= cum_sum * m:
                ans = max(ans, cum_sum)
print(ans)