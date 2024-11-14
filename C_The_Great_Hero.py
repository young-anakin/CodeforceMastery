t = int(input())
import math
for _ in range(t):
    a, b, n = list(map(int, input().split(" ")))
    attack = list(map(int, input().split(" ")))
    health = list(map(int, input().split(" ")))
    fl = True
    for ind in range(len(attack)):
        if ind == n-1:
            rr = math.ceil(health[ind]/a)
            b -= rr * attack[ind]
            if b + attack[ind] > 0:
                break
            else:
                fl = False
                break

        rounds = math.ceil(health[ind]/a)
        b -= rounds * attack[ind]
        if b < 0:
            fl = False
            break    
    # print(b)

    if fl:
        print("YES")
    else:
        print("NO")
                

