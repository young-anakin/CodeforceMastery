t = int(input())
val = input()
from collections import Counter
cp = Counter(val)
arr = []

while cp['n'] > 0:
    arr.append(1)
    cp['n'] -=1

while cp['z'] > 0:
    arr.append(0)
    cp['z'] -=1

print(*arr)