n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
from collections import deque
q = deque(u+d)
t = t % (2*n)
q.rotate(t)
q = list(q)
print(*q[:n])
print(*q[n:])