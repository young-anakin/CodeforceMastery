n, k = list(map(int, input().split(" ")))
arr = list(map(str, input().split(" ")))
from collections import defaultdict
cp = 0
for ind in arr:
    val = list(ind)
    # dd = defaultdict(val)
    if val.count('4') + val.count('7') <= k:
        cp +=1
print(cp)