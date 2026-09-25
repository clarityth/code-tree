N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
ans = 0
jewels = [[0]*3 for _ in range(N)]

for i, (weight, value) in enumerate(zip(w, v)):
    jewels[i][0] = weight
    jewels[i][1] = value
    jewels[i][2] = value/weight

jewels.sort(key=lambda x: -x[2])

remain_bag = M
for weight, value, _ in jewels:
    if remain_bag > weight:
        remain_bag -= weight
        ans += value
    else:
        avail_ratio = remain_bag / weight
        remain_bag -= avail_ratio*weight
        ans += avail_ratio*value

print(f"{round(ans,3):.3f}")
