import heapq
from math import ceil

Q = int(input())
cmds = [input() for _ in range(Q)]

lamp_dist = [] # 인접한 두 가로등 사이의 거리를 저장하는 pq
lamp_pos = {}
prev = {}
next = {}

insert_idx = -1
deleted = set() # 삭제된 가로등 idx 저장

N = -1 # 거리의 크기

for cmd in cmds:
    cmd = list(map(int, cmd.split()))
    operator = cmd[0]

    # 마을 상태 확인
    if operator == 100:
        N = cmd[1] # 거리의 크기
        M = cmd[2] # 초기 존재 가로등 갯수
        lamps = cmd[3:]

        # 초기 가로등 (1,2,⋯,M번)
        for i in range(len(lamps)):
            idx = i+1
            lamp_pos[idx] = lamps[i] # 자기 위치
            prev[idx] = -1 if idx == 1 else idx-1 # 왼쪽 가로등 idx
            next[idx] = -1 if idx == M else idx+1 # 오른쪽 가로등 idx

            if i != len(lamps)-1:
                lamp_dist.append([
                    -(lamps[i+1]-lamps[i]), 
                    (lamps[i], lamps[i+1]), 
                    idx,
                    idx+1
                ]) # (거리, 좌표 값(가로등1, 가로등2), 가로등1 idx, 가로등2 idx) 
        
        heapq.heapify(lamp_dist)

        insert_idx = M+1
        head = 1
        tail = M


    # 가로등 추가
    elif operator == 200:
        # 삭제된 원소 제거    
        while lamp_dist and (lamp_dist[0][2] in deleted or lamp_dist[0][3] in deleted):
            heapq.heappop(lamp_dist)
        
        (max_dist, (left_pos, right_pos), left_idx, right_idx) = heapq.heappop(lamp_dist)
        max_dist = -max_dist # 양수 전환

        # 나누어 떨어짐
        if (left_pos+right_pos) / 2 == (left_pos+right_pos) // 2:
            insert_pos = (left_pos+right_pos) // 2
        # 나누어 떨어지지 않음
        else:
            insert_pos = ceil((left_pos+right_pos)/2)

        # (거리, 좌표 값(가로등1, 가로등2), 가로등1번호, 가로등2번호) 
        heapq.heappush(lamp_dist, 
                        [-1*(insert_pos-left_pos), 
                        (left_pos, insert_pos), 
                        left_idx, 
                        insert_idx]) # 왼쪽 가로등 - 새로운 가로등

        heapq.heappush(lamp_dist, 
                        [-1*(right_pos-insert_pos), 
                        (insert_pos, right_pos), 
                        insert_idx, 
                        right_idx]) # 새로운 가로등 - 오른쪽 가로등

        lamp_pos[insert_idx] = insert_pos
        
        # linked list 재정의
        next[left_idx] = insert_idx
        prev[right_idx] = insert_idx
        next[insert_idx] = right_idx
        prev[insert_idx] = left_idx

        insert_idx += 1
        # print(lamp_dist)

    # 가로등 제거
    elif operator == 300:
        D = cmd[1]

        # 삭제 set에 추가
        deleted.add(D)

        # linked list 재정의
        left_idx = prev[D]
        right_idx = next[D]

        if left_idx == -1:
            head = right_idx
        else:
            next[left_idx] = right_idx

        if right_idx == -1:
            tail = left_idx
        else:
            prev[right_idx] = left_idx
        
        # D 제거
        del lamp_pos[D] 
        del next[D]
        del prev[D]

        # 가운데 가로등을 삭제한 경우
        if left_idx != -1 and right_idx != -1:
            left_pos = lamp_pos[left_idx]
            right_pos = lamp_pos[right_idx]
            new_dist = right_pos - left_pos
            
            heapq.heappush(lamp_dist, 
                            [-new_dist, 
                            (left_pos, right_pos), 
                            left_idx, 
                            right_idx])
        
    # 최소 전력 계산
    elif operator == 400:
        ans = float('inf')
        
        # 삭제된 원소 제거 
        while lamp_dist and (lamp_dist[0][2] in deleted or lamp_dist[0][3] in deleted):
            heapq.heappop(lamp_dist)
        
        max_dist = -1*lamp_dist[0][0] # 양수 변환
        start_dist = 2*(lamp_pos[head]-1) # 시작 ~ 첫번째 가로등 거리
        end_dist = 2*(N-lamp_pos[tail]) # 마지막 가로등 ~ 끝 거리
        max_dist = max(max_dist, start_dist, end_dist)
        ans = min(ans, max_dist)

        print(ans)