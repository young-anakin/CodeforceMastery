n = int(input())
import math
for ind in range(n):
    a,b,c = list(map(int, input().split(" ")))

    tot = a
    fl = True
    # print("TURN", ind)
    if b < 3 and b > 0:
        req = 3 - b
        if c < req:
            print(-1)
        else:
            tot += math.ceil((c+b)/3)
            print(tot)
    else:
        rem = b%3
        if rem == 0:
            tot += b//3
            tot += math.ceil(c/3)
            print(tot)
        else:
            if 3 - rem <= c:
                b += 3-rem
                c -= (3- rem)
                tot += b//3
                tot += math.ceil(c/3)
                print(tot)
            else:
                print(-1)