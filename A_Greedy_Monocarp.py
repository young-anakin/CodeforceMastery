t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    arr.sort(reverse=True)
    # print(arr)
    sm = sum(arr)
    if sm <= m:
        print(abs(m-sm))
        continue
    cp= 0
    for ind in arr:
        cp += ind
        if cp == m:
            rest = 0
            break
        elif cp > m:
            # print(cp)
            cp -= ind
            # print(cp)
            rest = abs(cp-m)
            break
    
    print(rest)