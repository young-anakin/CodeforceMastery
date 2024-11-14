from collections import deque
n = int(input())
arr = list(map(int, input().split(" ")))
odd = 0
even = 0
for ind in arr:
    if ind %2 == 0:
        even +=1
    else:
        odd +=1

if even > 0 and odd > 0:
    arr.sort()
    print(*arr)
else:
    print(*arr)
