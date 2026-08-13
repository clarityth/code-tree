from collections import deque

N, r, c, d = map(int, input().split())
print(r, c)

r -= 1
c -= 1
d -= 1

# 0: 바다, 1: 암초
grid = [list(map(int, input().split())) for _ in range(N)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우

# phase 1 방향별 탐색 방향 인덱스(직, 좌, 우, 후)
dirs_idx = [[0, 2, 3, 1], # 상 기준
            [1, 3, 2, 0], # 하 기준
            [2, 1, 0, 3], # 좌 기준
            [3, 0, 1, 2]] # 우 기준

# phase 2 우선순위: 좌/하/우/상
dirs_idx_p2 = [2, 1, 3, 0]

visited = set([(r, c)])
total = 0
for row in grid:
    for val in row:
        if val == 0:
            total += 1

cur_r, cur_c, cur_d = r, c, d

while len(visited) < total:
    # 1단계: 인접 탐험
    is_moved = False
    #  현재 바라보는 방향으로 직진 > 좌회전 > 우회전 > 180도 회전후 직진
    for idx in dirs_idx[cur_d]:
        next_r, next_c = cur_r + dirs[idx][0], cur_c + dirs[idx][1]
        if 0 <= next_r < N and 0 <= next_c < N and (next_r, next_c) not in visited and grid[next_r][next_c] == 0:
            cur_r, cur_c, cur_d = next_r, next_c, idx
            print(cur_r+1, cur_c+1)
            visited.add((next_r, next_c))
            is_moved = True
            break # 해당 방향으로 진행

    if is_moved:
        continue

    # 인접한 칸 모두에 방문 가능한 바다가 없다면
    # 2단계: 가장 가까운 바다로 이동 / 맨해튼 거리 최소 이동 -> bfs
    min_dist = float('inf')
    min_pos = (float('inf'), float('inf'))
    visited_2 = set([(cur_r, cur_c)])
    last_dir = cur_d

    q = deque([(cur_r, cur_c, cur_d, 0)])
    while q:
        c_r, c_c, c_dir, c_dist = q.popleft()

        # 행 번호 작은 > 열 번호 작은 우선 순위 반영 다음 이동 바다 갱신
        if (c_r, c_c) not in visited:
            if min_dist >= c_dist:
                min_dist = c_dist
                if min_pos[0] > c_r:
                    last_dir = c_dir
                    min_pos = (c_r, c_c)
                elif min_pos[0] == c_r:
                    if min_pos[1] > c_c:
                        last_dir = c_dir
                        min_pos = (c_r, c_c)
            continue

        # 좌, 하, 우, 상 순으로 이동 시도
        for idx in dirs_idx_p2:
            n_r, n_c = c_r+dirs[idx][0], c_c+dirs[idx][1]
            if 0 <= n_r < N and 0 <= n_c < N and grid[n_r][n_c] == 0 and (n_r, n_c) not in visited_2:
                q.append((n_r, n_c, idx, c_dist+1))
                visited_2.add((n_r, n_c))
    
    # 계산 결과, 가까운 바다를 기록
    cur_r, cur_c = min_pos[0], min_pos[1]
    visited.add((cur_r, cur_c)) # 방문 처리
    cur_d = last_dir
    print(cur_r+1, cur_c+1)
