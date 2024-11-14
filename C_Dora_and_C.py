t = int(input())
import bisect
for _ in range(t):
    n, a, b = list(map(int, input().split(" ")))
    a, b = min(a,b), max(a,b)
    arr = list(map(int, input().split(" ")))
    arr.sort()
    first = []
    second = []
    third = []
    mn = max(arr) - min(arr)
    for ind in arr:
        first.append(ind + a)
        second.append(ind + b)
        third.append(ind + a +b)
    
    for ind in first:
        x = bisect.bisect_left(second, ind)
        if x != 0:
            mn = min(mn, min(second[x] - ind, ind - second[x-1] ))
        else:
            mn = min(mn, second[x] - ind)
        x = bisect.bisect_left(third, ind)
        if x != 0:
            mn = min(mn, min( third[x] - ind,  ind - third[x-1]))
        else:
            mn = min(mn, third[x] - ind)
    print(mn)
    print(first, second, third)   