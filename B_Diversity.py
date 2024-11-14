val = list(input())
n = int(input())
aa = set(val)
from collections import Counter
cp = Counter(val)
# print(aa)
if len(aa) >= n:
    print(0)
elif n > len(val):
    print("impossible")
else:
    # if len(aa) >= n:
    #     print(0)
    # else:
    print(abs(n - len(aa)))
# print(aa)