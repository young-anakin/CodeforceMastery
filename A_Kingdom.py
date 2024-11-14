t, n = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
from collections import defaultdict
import heapq
arr = []
ss = set(a)
available = n - len(ss)
dd = defaultdict(int)
for ind in a:
    dd[ind] +=1

for ind, val in enumerate(a):
    if dd[val] > 1:
        heapq.heappush(arr, (b[ind], val))

ans = 0
cp = 0
while cp < available:
    tt = heapq.heappop(arr)
    # print(tt)
    if dd[tt[1]] > 1:
        dd[tt[1]] -=1
        ans += tt[0]
        cp +=1
    
print(ans)
# print(available)
