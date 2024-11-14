n = input()

arr = list(map(int , input().split(" ")))
from collections import Counter

cp = set(arr)
arr = list(cp)
ans = 0
arr.sort()

if 0 in arr:
    print(len(arr)-1)
else:
    print(len(arr))

