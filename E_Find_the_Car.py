import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right as br, bisect_left as bl, insort; from math import inf; from functools import lru_cache; from itertools import accumulate; import math; from heapq import heappop, heappush, heapify; from math import sqrt; ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip();

def solve():
    n, k, q = lip()
    a = [0] + lip()
    b = [0] + lip()
    arr = []
    for _ in range(q):
        d = ip()
        i = bl(a, d)
        ans = 0
        if i:
            ans = a[i - 1]
            d -= a[i - 1]
        if i == k:
            r = (a[-1] - a[-2]) / (b[-1] - b[-2])
        elif not i:
            r = a[1] / b[1]
        else:
            r = (a[i] - a[i - 1]) / (b[i] - b[i - 1])
        
        ans += d / r
        arr.append(int(ans))
    print(*arr)
    pass

t = ip()
for _ in range(t):
    solve()