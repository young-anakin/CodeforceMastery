n = int(input())
from collections import Counter, defaultdict
checker = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for ind in range(n):
    sz, k = list(map(int, input().split(" ")))
    val = input()
    alph = Counter(val)
    ans = 0
    for key, values in alph.items():
        if k == 0:
            break

        if key in checker:
            if alph[key.lower()] > alph[key]:
                
            ans += alph[key.lower()]

            alph[key.lower]
        

