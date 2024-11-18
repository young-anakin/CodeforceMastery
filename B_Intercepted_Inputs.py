t = int(input())
from collections import Counter
for _ in range(t):
    n  = int(input())
    arr = list(map(int, input().split(" ")))
    cp = Counter(arr)
    x = n-2
    a, b = 0,0
    for ind in arr:
        rest = x/ ind
        if rest == int(rest):
            if cp[rest] >= 1:
                if cp[rest] == 1:
                    if rest != ind:
                        a = int(rest)
                        b = ind
                    else:
                        continue
                else:
                    a = int(rest)
                    b = ind
        else:
            continue
    print(a, b)