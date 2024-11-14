n = int(input())
from collections import Counter

for _ in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))
    cp = Counter(arr)
    val = max(cp.values())
    print(sz - val)