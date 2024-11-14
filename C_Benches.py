t = int(input())
arr = []
k = int(input())
for _ in range(t):
    val = int(input())
    arr.append(val)
j = max(arr) + k

import math
rem = 0
mx = max(arr)
for ind in range(len(arr)):
    rem += mx - arr[ind]

if k >= rem:
    k -= rem
    tmp = math.ceil(k/t)
    # print(tmp)
    print( max(arr) + tmp, j )
else:
    print(max(arr), j)