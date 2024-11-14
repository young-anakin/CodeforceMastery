n = int(input())
for _ in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))
    mx = 0
    cp = 0
    for ind in range(sz):
        if arr[ind] == 0:
            cp +=1
        else:
            mx = max(cp, mx)
            cp = 0
    mx = max(mx, cp)
    print(mx) 