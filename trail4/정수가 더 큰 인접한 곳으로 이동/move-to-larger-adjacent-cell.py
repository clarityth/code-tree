n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] #(dr, dc)
q = deque([(r, c)])
record = [a[r][c]]

while q:
    cr, cc = q.popleft()
    for i in range(4):
        nr, nc = cr+dirs[i][0], cc+dirs[i][1]
        if 1 <= nr <= n and 1 <= nc <= n and a[cr][cc] < a[nr][nc]:
            q.append((nr, nc))
            record.append(a[nr][nc])
            break

print(*record)