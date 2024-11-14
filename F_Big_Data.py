n = int(input())
import math

x = math.sqrt(n)

if int(x) == x:
    print(int(x*4))
    

else:
    mn = float("inf")
    # print(x)
    for ind in range(1, math.floor(x)+1):
        # print(n, ind)
        if n % ind == 0:
            mn = min((n//ind)  *2 + ind*2, mn)
    print(mn)