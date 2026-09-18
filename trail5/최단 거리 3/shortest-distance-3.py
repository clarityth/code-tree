n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

# Please write your code here.
from heapq import heappush, heappop
from collections import defaultdict
dist = [float('inf')]*(n+1)
dist[A] = 0
pq = [(0, A)]

graph = defaultdict(list)

for a, b, d in edges:
    graph[a].append((d, b))
    graph[b].append((d, a))

while pq:
    cur_dist, cur_dest = heappop(pq)

    if cur_dist > dist[cur_dest]:
        continue
    
    for next_dist, next_dest in graph[cur_dest]:
        new_dist = cur_dist + next_dist
        if dist[next_dest] > new_dist:
            dist[next_dest] = new_dist
            heappush(pq, (new_dist, next_dest))

print(dist[B])