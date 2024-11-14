n = int(input())
from collections import Counter
for _ in range(n):
    sz = int(input())
    val = input()
    cp = Counter(val)
    # print(cp)
    if cp['0'] == cp['1']:
        if sz <= 2:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")