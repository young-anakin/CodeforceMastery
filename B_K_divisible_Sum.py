t = int(input())
import math
for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    if n%k == 0:
        print(1)
    elif k >= n:
        print(math.ceil(k/n))
    else:
        print(2)