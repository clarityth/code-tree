from collections import deque
n, m, q = map(int, input().split())
a = [deque(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
def shift(row, dir):
    global a
    if dir == 'L':
        a[row].rotate(1)
    else:
        a[row].rotate(-1)

def propagate(row, push_dir, prop_dir):
    global a, m
    rev_push_dir = None
    if push_dir == 'L':
        rev_push_dir = 'R'
    else:
        rev_push_dir = 'L'

    if prop_dir == 'U':
        if 0 <= row-1 < n:
            if check(row, row-1):
                shift(row-1, rev_push_dir)
                propagate(row-1, rev_push_dir, prop_dir)

    elif prop_dir == 'D':
        if 0 <= row+1 < n:
            if check(row, row+1):
                shift(row+1, rev_push_dir)
                propagate(row+1, rev_push_dir, prop_dir)

def check(r1, r2):
    global a
    for i in range(m):
        if a[r1][i] == a[r2][i]:
            return True
    
    return False

for r, d in winds:
    r -= 1

    shift(r, d)
    propagate(r, d, 'U')
    propagate(r, d, 'D')

for row in a:
    print(*row)

