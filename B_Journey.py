t = int(input())
for _ in range(t):
    n, a, b, c = list(map(int, input().split(" ")))

    sm = a + c+b
    # print(n, sm)
    tot = n // sm
    cp = 0
    x = 0

    for ind in [a, b, c]:
        if x + (tot * sm) >= n:
            break
        x += ind
        if x + (tot * sm) >= n:
            cp +=1
            break
        else:
            cp +=1
    print(tot * 3 +  cp )