n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
from functools import cmp_to_key
str_arr = [0]*n
for i in range(n):
    str_arr[i] = str(arr[i])

def compare(a, b):
    if int(a+b) > int(b+a):
        return -1
    else:
        return 1

str_arr.sort(key=cmp_to_key(compare))
print(''.join(str_arr))