from collections import defaultdict
sz = int(input())
for ind in range(sz):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    occ = defaultdict(int)

    for i in range(n):
        occ[a[i]] +=1

    L, R = -1, -1
    l, r = -1, -1
    i = 0
    while i < n:
        if occ[a[i]] < k:
            i += 1
            continue
        if l == -1:
            l = a[i]
        if i == n - 1 or a[i + 1] - a[i] > 1 or occ[(a[i + 1])] < k:
            r = a[i]
            if r - l >= R - L:
                R = r
                L = l
            l = -1
            r = -1
        i += 1

    if L == -1:
        print(-1)
    else:
        print(L, R)

