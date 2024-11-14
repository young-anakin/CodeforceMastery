t = int(input())
for _ in range(t):
    n, a, b = list(map(int, input().split(" ")))
    
    minA, minB = 0,0
    while n > 0:
        if n > 1:
            minA += 2 * a
            minB += b
            n-=2
        else:
            minA += a
            minB += a
            n-=2
    # print(minA, minB)
    print(min(minA, minB))
