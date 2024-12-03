t = int(input())

import math, bisect
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()

    mx = bisect.bisect_left(arr, math.ceil(arr[-1]/2))
    mx = arr[mx]
    # print(mx)
    cp = 0
    for val in arr:
        if val < mx:
            cp +=1
    
    print(cp)
    # print(mx)
    # print(arr)