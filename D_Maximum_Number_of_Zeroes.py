n = int(input())
arr1 = list(map(int, input().split(" ")))
arr2 = list(map(int, input().split(" ")))
from collections import defaultdict
from math import gcd
cp = defaultdict(int)
special = 0
for ind in range(n):
    if arr1[ind] == 0:
        if arr2[ind] == 0:
            special +=1
        continue
    val = gcd(arr1[ind], arr2[ind])
    arr1[ind] /= val
    arr2[ind] /= val

    # if arr1[ind] == 0:
    if arr2[ind] < 0 and arr1[ind] > 0 or arr2[ind] > 0 and arr1[ind] < 0:
        cp[(-1 * abs(arr2[ind]), abs(arr1[ind]))] +=1
    else:
        cp[(abs(arr2[ind]), abs(arr1[ind]))] +=1
# print(cp)
if len(cp) != 0:
    mx = max(cp.values())
    print(mx+special)
else:
    print(special)