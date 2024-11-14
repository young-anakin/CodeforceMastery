t = int(input())
from collections import defaultdict
import math
v = 1
for _ in range(t):
    n, q = list(map(int, input().split(" ")))
    val1 = input()
    val2 = input()
    arr = [0]
    diff = 0
    dd = defaultdict(int)
    dd2 = defaultdict(int)
    for ind in range(n):
        add = 0
        sub = 0
        if val1[ind] == val2[ind]:
            arr.append(arr[-1])
        else:
            if dd2[val1[ind]] == 0:
                dd[val1[ind]] +=1
                add +=1
            else:
                dd2[val1[ind]] -=1
                sub -=1
            if dd[val2[ind]] == 0:
                dd2[val2[ind]] +=1
                add +=1
            else:
                dd[val2[ind]] -=1
                sub -=1
            arr.append(arr[-1] + (add + sub))
    # print(arr)
    for ind in range(len(arr)):
        arr[ind] = math.ceil(arr[ind]/2)
    print(arr)
    for ind in range(q):
        a, b = list(map(int, input().split(" ")))
        if a == b:
            if val1[a-1] == val2[b-1]:
                print(v, 0)
            else:
                print(v, 1)
            v+=1
            continue
        print((a,b), v, abs(arr[b] - arr[a-1]))
        v+=1
    # print(arr[1:])
