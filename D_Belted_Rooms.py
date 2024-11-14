t = int(input())
from collections import defaultdict
for _ in range(t):
    dd = defaultdict(list)
    n = int(input())
    arr = input()
    ss = set()
    for ind in range(len(arr)):
        if arr[ind] == '-':
            dd[arr[ind]]
        elif arr[ind] == ">":
            pass
        else:
            pass