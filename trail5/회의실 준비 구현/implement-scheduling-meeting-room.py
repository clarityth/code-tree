n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
meetings.sort(key=lambda x:x[1])

ans = 0
last_end = -1
for start_time, end_time in meetings:
    if start_time >= last_end:
        ans += 1
        last_end = end_time

print(ans)