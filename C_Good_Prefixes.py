t = int(input())
from collections import defaultdict

for x in range(t):
    subArrays = defaultdict(int)
    subArrays[0] +=1
    n = int(input())
    arr = list(map(int, input().split(" ")))
    ps = 0
    mx = 0
    cp = 0
    for ind in arr:
        ps += ind
        mx = max(mx, ind)
        # subArrays[ps] +=1
        # print(ps/2 == int(ps/2), subArrays[int(ps/2)])
        if ps-mx == mx:
            
            # print("Ya", ps, ind)
            cp +=1
    # print(subArrays)
    print(cp)