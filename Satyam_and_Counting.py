t = int(input())
from collections import defaultdict

for _ in range(t):
    x = []
    y = []
    n = int(input())
    dd = defaultdict(int)
    ss = defaultdict(int)
    for _ in range(n):
        a, b = list(map(int, input().split(" ")))
        dd[b] +=1
        ss[a] +=1
    x.sort()
    y.sort()
    # print(x , y)
    tot = 0
    for key, item in ss.items():
        if item > 1:
            tot += dd[0]-1
            tot += dd[1] - 1
    # print(dd, ss)
    print(tot)