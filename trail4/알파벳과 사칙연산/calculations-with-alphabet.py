expression = input()

# Please write your code here.
from itertools import product

alphas = []
ops = []

for c in expression:
    if c.isalpha():
        alphas.append(c)
    else:
        ops.append(c)

unique_alphas = list(set(alphas))
ans = -float('inf')
temp = None

for pair in product(range(1, 5), repeat=len(unique_alphas)):
    seq = 0
    alpha_dict = {}
    for num in pair:
        alpha_dict[unique_alphas[seq]] = num
        seq += 1
    
    left = alpha_dict[alphas[0]]
    seq = 1
    for op in ops:
        right = alpha_dict[alphas[seq]]
        seq += 1
        if op == '+':
            left += right
        elif op == '-':
            left -= right
        elif op == '*':
            left *= right
    ans = max(ans, left)

print(ans)