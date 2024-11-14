n = int(input())
from collections import defaultdict
for ind in range(n):
    x = int(input())
    arr = list(map(int, input().split(" ")))
    # alph = ""
    alphCount = defaultdict(list)
    for y in range(97, 97+26):
        # alph += chr(y)
        alphCount[0].append(chr(y))
    # print(alphCount) 
    ans = []
    for z in range(x):
        val = alphCount[arr[z]].pop()
        # print(alphCount)
        alphCount[arr[z]+1].append(val)
        ans.append(val)
    print("".join(ans))