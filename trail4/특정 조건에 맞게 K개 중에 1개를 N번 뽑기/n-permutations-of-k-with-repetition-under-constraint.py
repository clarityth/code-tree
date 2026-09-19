K, N = map(int, input().split())

# Please write your code here.
def dfs(depth, pre_val, combo, record):
    global N
    if len(record) == N:
        print(*record)
        return

    for i in range(1, K+1):
        if pre_val == i and combo < 2:
            record.append(i)
            dfs(depth+1, i, combo+1, record)
            del record[depth]

        elif pre_val != i:
            record.append(i)
            dfs(depth+1, i, 1, record)
            del record[depth]

from collections import defaultdict
dfs(0, None, 0, [])