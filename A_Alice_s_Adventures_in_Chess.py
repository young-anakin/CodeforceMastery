t = int(input())
for _ in range(t):
    n, x, y = list(map(int, input().split(" ")))
    s = input()
    a, b = 0,0
    visited = set()

    N = (0,1)
    E = (1, 0)
    W = (-1, 0)
    S = (0, -1)

    # visited.add(a,b)
    if a == x and b == y:
        print("YES")
    else: 
        fl = False
        for _ in range(10000):
            for ind in s:
                if ind == "N":
                    a, b = a + N[0], b + N[1]
                if ind == "E":
                    a, b = a + E[0], b + E[1]
                if ind == "W":
                    a, b = a + W[0], b + W[1]
                if ind == "S":
                    a, b = a + S[0], b + S[1]
                
                # visited.add(a,b)
                if a == x and b == y:
                    fl = True
                    break
            

        if fl:
            print("YES")
        else:
            print("NO") 

import math

math.isP