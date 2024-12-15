t = int(input())
import math
for _ in range(t):
    x, y = list(map(int, input().split(" ")))
    cp = 0
    tot = 0

    while y > 0:
        if y >= 2:
            y -=2
            x -= 7
        elif y == 1:
            y -=1
            x -= 11
        cp +=1
    
    if x > 0:
        cp += math.ceil(x/15)
    
    print(cp)



