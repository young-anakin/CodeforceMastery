import math
t = int(input())
for p in range(t):
    n, k = list(map(int, input().split(" ")))
    if p == 
    if k == 1:
        print(1)
    elif n == k:
        print(1)
    elif n > k:
        print(math.ceil(n/k))
    else:
        print(math.ceil(k/n))