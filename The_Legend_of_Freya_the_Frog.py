t = int(input())
import math
for _ in range(t):
    x, y, k = list(map(int, input().split(" ")))
    tot = max(x//k, y//k) * 2
    # print(x, y, x//k * k, y//k * k)


    if y >= x:
        print(math.ceil(y/k)*2)
    else:
        # print(x, y)
        # print(tot)
        tot = max(x//k, y//k) * 2
        # print(x, y, x//k * k, y//k * k)
        x = x - (x//k * k)
        y = y - (y//k * k)
        # print(x, y, x//k * k, y//k * k)
        if y != 0:
            print(tot + (math.ceil((x/k)) *2))
        else:

            print(tot + (math.ceil((x/k)) *2)-1)