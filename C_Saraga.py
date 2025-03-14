first = input()
second = input()

from collections import defaultdict

firstoccurence = defaultdict(lambda: -float("inf"))

for i in range(len(second)-1):
    firstoccurence[second[i]] = i


mx = float("inf")
ans = ""
for i in range(1, len(first)):
    if firstoccurence[first[i]] ==-float("inf"):
        continue
    else:
        total = i + firstoccurence[first[i]]
        tmp = firstoccurence[first[i]]
        if mx >= len(first[:i] + second[tmp:]):
            ans = first[:i] + second[tmp:]
            mx = len(first[:i] + second[tmp:])
        
        # print(first[i], total, first[:i] + second[tmp:])
        # print(second[i+1:], )

if mx == float("inf"):
    print(-1)
else:

    print(ans)