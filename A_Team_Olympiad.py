n = int(input())
from collections import defaultdict
dd = defaultdict(list)
arr = list(map(int, input().split(" ")))
for ind in range(n):
    dd[arr[ind]].append(ind+1)

x = min(len(dd[1]), len(dd[2]), len(dd[3]))
if x == 0:
    print(0)
else:
    print(x)
    for ind in range(x):
        print(dd[1].pop(), dd[2].pop(), dd[3].pop())