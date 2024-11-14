t = int(input())
from collections import defaultdict
state = defaultdict(int)
for ind in range(t):
    n,m,i1,j1,i2,j2,d = list(map(int, input().split(" ")))
    fl = True
    bounce = 0
    while True:
        if d == "DL":
            if state[(i1, j1, d)] == 1:
                fl = False
                break
            else:
                state[(i1, j1, d)] +=1

            if i1 + 1 >= 1 and j1 -1 >= 1:
                i1 +=1
                j1 -=1

                if i1 == i2 and j1 == j2:
                    break
            elif i1 + 1 > n:
                d = "UL"
            elif j1-1 < 1:
                d = "DR"
        elif d == "UL":
            if state[(i1, j1, d)] == 1:
                fl = False
                break
            else:
                state[(i1, j1, d)] +=1


            if i1 - 1 >= m and j1 - 1 >= 1:
                i1 -=1
                j1 -=1

                if i1 == i2 and j1 == j2:
                    break
            elif i1 + 1 > n:
                d = "UL"
            elif j1-1 < 1:
                d = "DR"




        if i1 == i2 and j1 == j2:
            break