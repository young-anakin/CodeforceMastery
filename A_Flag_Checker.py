n, m = list(map(int, input().split(" ")))
from collections import defaultdict, Counter
dd = defaultdict(int)
fl = True
last = -12
for ind in range(n):
    val = input()
    cp = Counter(val)
    if len(cp) > 1:
        fl = False
        break        
    if val[0] == last:
        fl = False
        break
    last = val[0]


if fl:
    print("YES")
else:
    print("NO")
     
