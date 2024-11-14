t = int(input())
from collections import defaultdict
for _ in range(t):
    n, m = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    dd = defaultdict(list)
    visited = set()
    i = 1
    if m <= n:
        print(-1)
    else:
        tot = []
        m -= n
        sm  = sum(arr) * 2
        # arr.sort()
        mn = min(arr)
        sub = sorted(arr)
        # print(sub)
        mx = arr[1]
        sm += ((mn * m) * 2)
        print(sm)
        for ind in range(n-1):
            print(ind+1, ind+2)
        
        print(n, 1)
 
        mn = arr.index(mn)
        mx = arr.index(mx)
        for ind in range(m):
            print(mn+1, mx+1)