n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
from collections import deque
q = deque(l+r+d)
q.rotate(t%(3*n))
ans = list(q)
print(*ans[:n])
print(*ans[n:2*n])
print(*ans[2*n:])