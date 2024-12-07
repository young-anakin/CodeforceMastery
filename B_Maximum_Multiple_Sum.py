t = int(input())
for _ in range(t):
    n = int(input())

    mx = float("inf") * -1
    ans = 0
    for ind in range(1, n+1):
        i = ind
        cp = 0
        sm = 0
        x = 1
        while x*ind < n:
            sm += (x * ind)
            x +=1
            cp +=1

        if sm > mx:
            mx = max(mx, sm)
            ans = ind
    print()
    print(ans)


