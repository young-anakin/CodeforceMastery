s = input()
from collections import defaultdict
dd = defaultdict(int)
for ind in range(len(s)):
    i = 1

    while i + ind <= len(s):
        dd[s[ind:ind+i]] +=1
        i +=1

mx = 0
for key, val in dd.items():
    if val >= 2:
        mx = max(mx, len(key))
print(mx)