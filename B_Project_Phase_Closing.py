n, m , k = list(map(int, input().split(" ")))
d, r = 1, 1
for ind in range(n*m*2):
    k -= 2
    if k <= 0:
        if k == 0:
            print( r, d, 'R')
        else:
            print(r, d, "L")
        break
    else:
        d +=1
        if d > m:
            r += 1
            d = 1
            continue
