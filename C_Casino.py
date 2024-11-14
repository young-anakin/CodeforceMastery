n = int(input())
from math import gcd
arr = list(map(int, input().split(" ")))
# print(arr)
ll = gcd(*arr)
fl = True
for ind in range(len(arr)):
    val = arr[ind]//ll
    # print(val)
    while val %2 == 0:
        val /= 2
    
    while val %3 == 0:
        val /= 3

    if val != 1:
        fl = False
        break

if fl:
    print("YES")
else:
    print("NO")