N, M, K = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)] # 0: 빈 공간 1: 산호초 2: 화산 3: 다른 바다 거북 4: 화석
turtles = [list(map(int, input().split())) for _ in range(M)]
volcanoes = [list(map(int, input().split())) for _ in range(K)]
volcano_pos_to_idx = {} # 화산 좌표 -> 인덱스 매핑

# 맵 화산 표시
for idx, volcano in enumerate(volcanoes):
    row = volcano[0]
    col = volcano[1]
    sea[row][col] = 2
    volcano_pos_to_idx[(row, col)] = idx

# 맵 다른 바다거북 표시
for turtle in turtles:
    row = turtle[0]
    col = turtle[1]
    sea[row][col] = 3

res = [-1] * len(turtles)

# 우하좌상 델타
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

from collections import deque

pressures = [0] * len(volcanoes) # 각 화산의 압력을 저장

for t in range(1, 101):
    heat = [[0]*N for _ in range(N)] # 전체 맵의 열기를 저장 (매턴마다 열기 정보 초기화)
    
    # 1단계: 바다거북 이동
    for turtle_idx, turtle in enumerate(turtles):
        turtle_row, turtle_col = turtle[0], turtle[1]
        
        # 화석이거나 이미 도착했다면 건너뜀
        if sea[turtle_row][turtle_col] == 4 or res[turtle_idx] != -1:
            continue

        is_moved = False
        
        q = deque([(turtle_row, turtle_col, None, None)]) # 현재 row, 현재 col, 시작 row, 시작 col
        visited = set([(turtle_row, turtle_col)])
        
        # bfs: 거북이 -> 안식처 최단경로 탐색
        while q:
            cur_row, cur_col, first_step_row, first_step_col = q.popleft()

            # 최단경로 탐색 종료
            if (cur_row, cur_col) == (N-1, N-1) and first_step_row != None and first_step_col != None: 
                # 다음 위치로 한 스텝 이동
                turtle[0], turtle[1] = first_step_row, first_step_col
                break

            for i in range(4):
                next_row, next_col = cur_row+dr[i], cur_col+dc[i]

                if 0 <= next_row < N and 0 <= next_col < N:
                    # 산호초, 다른 거북(맵 표시가 거북이면서 자신이 아님), 화석 통과 불가 / 화산 통과 가능
                    sea_val = sea[next_row][next_col]
                    if sea_val == 1 or ((next_row, next_col) != (turtle_row, turtle_col) and sea_val == 3) or sea_val == 4:
                        continue

                    if (next_row, next_col) not in visited:
                        if first_step_row == None and first_step_col == None:
                            q.append((next_row, next_col, next_row, next_col))
                        else :
                            q.append((next_row, next_col, first_step_row, first_step_col))
                        visited.add((next_row, next_col))
                        is_moved = True

        # 바다거북이 이동했다면 이동전 위치 초기화 / 새로운 위치 표시
        if is_moved:
            sea[turtle_row][turtle_col] = 0
            sea[turtle[0]][turtle[1]] = 3

        # 안식처에 최종 도달했다면
        if (turtle[0], turtle[1]) == (N-1, N-1):
            res[turtle_idx] = t # 결과 기록
            sea[N-1][N-1] = 0 # 안식처에 거북이 치우기


    erupted_idx = [] # 분출한 화산의 인덱스 저장
    erupted_pos = set() # 분출한 화산의 좌표 저장

    # 2단계: 화산 압력 증가
    for i in range(len(pressures)):
        pressures[i] += 10
        # 각 화산의 분출 임계치(P) 이상인 화산은 뜨거운 열기를 분출
        if pressures[i] >= volcanoes[i][2]:
            erupted_idx.append(i)
            erupted_pos.add((volcanoes[i][0], volcanoes[i][1]))
    
    # 3단계: 화산 분출 및 연쇄 반응
    # 한 칸에 여러 화산의 열기가 도달하면 그 값들을 모두 합산
    volcano_q = deque(erupted_idx)

    while volcano_q:
        volcano_idx = volcano_q.popleft()
        v_row = volcanoes[volcano_idx][0]
        v_col = volcanoes[volcano_idx][1]
        v_threshold = volcanoes[volcano_idx][2]
        heat[v_row][v_col] += v_threshold

        # 1. 열기 전파: 분출 임계치(P) 만큼의 열기가 발생
        # 상하좌우
        for i in range(4):
            h_row = v_row
            h_col = v_col
            heat_val = v_threshold
            
            # 산호초(1)를 만나거나 열기 값이 0이 되면 해당 방향의 전파는 중단
            while (0 <= h_row < N and 0 <= h_col < N and sea[h_row][h_col] != 1 and heat_val > 0):
                h_row += dr[i]
                h_col += dc[i]

                if h_row < 0 or h_row >= N or h_col < 0 or h_col >= N:
                    continue

                # 한 칸 이동할 때마다 열기 반감
                heat_val = heat_val // 2 
                heat[h_row][h_col] += heat_val
                
                # 2. 연쇄 반응
                if sea[h_row][h_col] == 2 and (h_row, h_col) not in erupted_pos: # 아직 분출하지 않은 화산이라면
                    target_idx = volcano_pos_to_idx[(h_row, h_col)]
                    
                    # (압력 + 누적 열기) ≥ 분출 임계치(P) -> 즉시 분출 시작
                    if pressures[target_idx] + heat[h_row][h_col] >= volcanoes[target_idx][2]:
                        volcano_q.append(volcano_pos_to_idx.get((h_row, h_col)))
                        erupted_idx.append(target_idx)
                        erupted_pos.add((h_row, h_col))

    # 3. 화석화
    # 총 열기 합 >= 20이면 화석화
    for turtle_idx, turtle in enumerate(turtles):
        turtle_row = turtle[0]
        turtle_col = turtle[1]
        if sea[turtle_row][turtle_col] == 4 or res[turtle_idx] != -1: # 이미 화석이거나 도착
            continue

        if heat[turtle_row][turtle_col] >= 20:
            sea[turtle_row][turtle_col] = 4
    
    # 4. 환경 초기화
    # 이번 턴에 분출한 모든 화산 압력 초기화
    for idx in erupted_idx:
        pressures[idx] = 0
    
for turn in res:
    print(turn)