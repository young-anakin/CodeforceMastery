n = int(input())
from collections import Counter
arr = []
for ind in range(n):
    val = input()
    arr.append(val)
cp = Counter(arr)
print(max(cp, key= cp.get))