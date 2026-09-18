n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from heapq import heappush, heappop
from collections import defaultdict

graph = defaultdict(list)

for a, b, d in edges:
    graph[a].append((d, b))

dist = [float('inf')] * (n+1)
dist[1] = 0

pq = [(0, 1)]
while pq:
    cur_dist, cur_dest = heappop(pq)
    if cur_dist > dist[cur_dest]:
        continue
    
    for next_dist, next_dest in graph[cur_dest]:
        new_dist = cur_dist + next_dist
        if new_dist < dist[next_dest]:
            dist[next_dest] = new_dist
            heappush(pq, (new_dist, next_dest))

for i in range(2, n+1):
    if dist[i] != float('inf'):
        print(dist[i])
    else:
        print(-1)