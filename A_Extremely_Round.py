t = int(input())
from collections import Counter
ans = [0]
for ind in range(1, 100):
    val = str(ind)
    cp = 0

    dd = Counter(val)

    if dd['0'] == len(val) - 1:
        ans.append(ans[-1] + 1)
    else:
        ans.append(ans[-1] + 1)

print(ans)