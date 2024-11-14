t = int(input())
from collections import Counter
for _ in range(t):
    n = int(input())
    val = input()
    cp = Counter(val)
    tot = 0
    tot += min(cp['A'], n)
    tot += min(cp['B'], n)
    tot += min(cp['C'], n)
    tot += min(cp['D'], n)
    print(tot)
    
