n = int(input())
from collections import defaultdict
from math import ceil
for ind in range(n):
    sz, k = list(map(int, input().split(" ")))
    resource = list(map(int, input().split(" ")))
    time = list(map(int, input().split(" ")))
    dd = defaultdict(int)
    for z in range(sz):
        dd[resource[z]] = time[z]
    else:
        mn = 0
        mx = max(resource)
        ans = float("inf")
        while (mn+1) < mx:
            md = (mn + mx)//2
            tot = 0
            # print(mn, mx, md)
            for t in range(sz):
                tot += ceil((resource[t]/md)) * time[t]
                # if resource[t]%md > 0:
                #     tot += dd[resource[t]]
            print("md", md, "Tot", tot)
            if tot > k:
                mn = md
            else:
                ans = min(ans, md)
                mx = md
        if ans == float("inf"):
            print(-1)
        else:
            print(ans)

