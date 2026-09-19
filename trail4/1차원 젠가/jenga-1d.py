n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
s1, e1, s2, e2 = s1-1, e1-1, s2-1, e2-1

blocks = blocks[:s1]+blocks[e1+1:]
blocks = blocks[:s2]+blocks[e2+1:]

if blocks:
    print(len(blocks))
    for i in range(len(blocks)):    
        print(blocks[i])

else:
    print(0)