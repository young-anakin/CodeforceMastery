n = int(input())
arr = list(map(int, input().split(" ")))

m = int(input())
q = list(map(int, input().split(" ")))


new = []
from collections import defaultdict
dd = defaultdict(int)
for ind in range(len(arr)):
    if ind == 0:
        new.append(1)
        new.append(arr[ind])
        # dd[1] = ind
        # dd[arr[ind]] = ind
    else:
        vl = new[-1]
        new.append(vl + 1)
        new.append(vl + arr[ind])
        # dd[vl+1] = ind
        # dd[vl+arr[ind]] = ind

import bisect

for j in range(m):
    sub = bisect.bisect_left(new, q[j])
    print((sub//2)+1)


