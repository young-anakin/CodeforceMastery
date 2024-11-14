t = int(input())
from collections import defaultdict
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    for i in range(1, 58):
        dd = defaultdict(int)
        
        for ind in arr:
            # print(ind, pow(2, i), ind% pow(2, i) )
            dd[ind% pow(2, i)  ] +=1
        if len(dd) == 2:
            # print(dd)
            print(pow(2, i))
            break