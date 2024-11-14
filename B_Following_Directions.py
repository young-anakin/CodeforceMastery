t = int(input())
from collections import defaultdict
dir = defaultdict(tuple)
dir['U'].append((1, 0))
dir['R'].append((0,1))
dir['D'].append((-1, 0))
dir['L'].append((0, -1))
for _ in range(t):
    n = int(input())
    val = input()
    og = (0,0)
    fl = False
    for i in range(n):
        if val[i] == 'U':
            og[0], og[1] = og[0]+dir['U'][0], og[1] + dir['U'][1]
        elif val[i] == "D":
            og[0], og[1] = og[0]+dir['D'][0], og[1] + dir['D'][1]
        elif val[i] == "R":
            og[0], og[1] = og[0]+dir['R'][0], og[1] + dir['R'][1]
        else:
            og[0], og[1] = og[0]+dir['L'][0], og[1] + dir['L'][1]
        if og == (1,1):
            fl = True
            break
    if fl:
        print("Yes")
    else:
        print("No")

            
