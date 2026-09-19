n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

# Please write your code here.
from collections import deque, defaultdict
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
alive = [True]*len(r)
cur_pos = []

for (row, col) in zip(r, c):
    cur_pos.append((row-1, col-1))

while t > 0:
    pos_cnt = defaultdict(int)
    # 구슬 이동
    for i, (cr, cc) in enumerate(cur_pos):
        if alive[i]:
            # 최대 값, 우선순위 탐색
            max_val = -float('inf')
            max_pos = None
            for j in range(4):
                nr, nc = cr+dirs[j][0], cc+dirs[j][1]
                if 0 <= nr < n and 0 <= nc < n:
                    if max_val < a[nr][nc]:
                        max_val = a[nr][nc]
                        max_pos = (nr, nc)

            # 실제 이동
            cur_pos[i] = max_pos
            pos_cnt[max_pos] += 1

    # 충돌 판정
    for i, pos in enumerate(cur_pos):
        if alive[i] and pos_cnt[pos] >= 2:
            alive[i] = False

    t -= 1

print(sum(alive))
