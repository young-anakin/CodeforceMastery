t = int(input())
import math
for _ in range(t):
    n = int(input())
    if n%2 == 1:
        print(math.ceil(n/2))
    else:
        print(n//2)