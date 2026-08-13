from bisect import bisect_left

Q = int(input())
tasks = [list(map(int, input().split())) for _ in range(Q)]

idx = 1
perfumes = {}
    
for task_idx, task in enumerate(tasks):
    if task_idx == 0 and task[0] == 1: # 향료 준비
        n = task[1]
        for i in range(2, 2+n):
            perfumes[idx] = task[i]
            idx += 1

    elif task[0] == 2: # 향료 추가(v)
        perfumes[idx] = task[1]
        idx += 1
    
    elif task[0] == 3: # 향료 폐기(idx)
        perfume_idx = task[1]
        deleted_degree = perfumes.get(perfume_idx, -1)
        if deleted_degree == -1: # 이미 폐기됐거나 존재하지 않는 번호라면 -1 출력
            print(-1)
        else:
            del perfumes[int(task[1])] # 폐기
            print(deleted_degree) # 폐기 향도 출력

    elif task[0] == 4: # 블렌딩(K)
        K = task[1]

        dp = [float('inf')]*(K+1) # 향도를 만족하는 최소 향수 갯수를 저장
        dp[0] = 0
        degrees = list(perfumes.values())

        # bounded knapsack
        for total_degree in range(1, K+1): # 누적 향도
            for degree in degrees: # 현재 향도
                if total_degree >= degree:
                    # 저장된 값, 현재 향도를 고르지 않았을 때의 최소 갯수 + 현재 향도를 골랐을때(1) 중 최솟값 저장
                    dp[total_degree] = min(dp[total_degree-degree]+1, dp[total_degree]) 
        
        print(dp[K] if dp[K] != float('inf') else -1) # 만들 수 있다면 최소 갯수, 없다면 -1 출력
    
    elif task[0] == 5: # 향수 구성(K)
        K = task[1]

        # 이진 탐색
        degrees = list(perfumes.values())
        degrees.sort()

        perfume_cnt = len(degrees)
        cnt = 0

        # top과 middle을 선택
        for top in degrees:
            for middle in degrees:
                base_min_idx = bisect_left(degrees, K-top-middle) # 이진 탐색으로 base 향도의 하한의 위치를 찾음
                cnt += (perfume_cnt-base_min_idx) # 하한보다 큰 향도의 향수의 갯수를 누적
        print(cnt)