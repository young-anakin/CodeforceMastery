t = int(input())
from collections import Counter
for _ in range(t):
    n = int(input())
    val = input()
    cp = Counter(val)
    arr = ['t', 'r', 'y', 'g', 'u', 'b']
    arr = arr[::-1]
    ans = []
    for a in arr:
        while cp[a] != 0:
            ans.append(a)
            cp[a] -=1
    
    for a in val:
        while cp[a] != 0:
            ans.append(a)
            cp[a] -=1
    pp = "".join(ans)
    print(pp)
