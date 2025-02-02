t = int(input())
# calculate the time it takes to 0 for each
from collections import Counter
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    cp= Counter(arr)
    mx = 0
    fl = False
    if 0 not in arr:
        print(0)
    else:
        # print(arr)
        for ind in range(1, len(arr)):
            # print(arr[ind], arr[ind-1])
            if abs(arr[ind] - arr[ind-1]) <= 1:
                continue
            else:
                mx = arr[ind-1] + 1
                fl = True
                break
        # print(cp)  
        if not fl:
            mx = max(arr) + 1
        ss = list(set(arr))
        xx = list()
        # print(ss, mx)
        for ind in ss:
            xx.append((ind, (mx * (cp[ind]-1) + ind) + (cp[0] - 1) * ind ))
        
        mn = float("inf")
        for x,y in xx:
            mn = min(mn, y)
        print(xx)
        print(mn)
        # cp = Counter(arr)
        # print(cp)
    # for ind in arr: