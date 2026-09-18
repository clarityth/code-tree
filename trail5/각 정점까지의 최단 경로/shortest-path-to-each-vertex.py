n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import defaultdict
from heapq import heappush, heappop

graph = defaultdict(list)
for a, b, d in edges:
    graph[a].append((d, b))
    graph[b].append((d, a))

pq = [(0, k)]
dist = [float('inf')]*(n+1)
dist[k] = 0

while pq:
    cur_c, cur_d = heappop(pq)
    if dist[cur_d] < cur_c:
        continue
    
    for next_c, next_d in graph[cur_d]:
        new_c = cur_c + next_c
        if dist[next_d] < new_c:
            continue
        
        dist[next_d] = new_c
        heappush(pq, (new_c, next_d))

for i in range(1, len(dist)):
    if dist[i] != float('inf'):
        print(dist[i])
    else:
        print(-1)