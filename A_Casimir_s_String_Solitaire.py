n = int(input())
from collections import Counter
for ind in range(n):
    val = input()
    dd = Counter(val)
    if dd["A"] + dd["C"] == dd["B"]:
        print("YES")
    else:
        print("NO")