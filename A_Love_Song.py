n, t = list(map(int, input().split(" ")))
val = input()
from collections import defaultdict
x = "abcdefghijklmnopqrstuvwxyz"
cp = 1
dd = defaultdict(int)
arr = []
for ind in val:
    if ind not in dd:
        dd[ind] = x.index(ind)+1
        cp +=1
        arr.append(dd[ind])
    else:
        arr.append(dd[ind])
    
prefix = [0]
for ind in range(len(arr)):
    prefix.append(prefix[-1] + arr[ind])

# print(arr)
# print(prefix)
for ind in range(t):
    a, b = list(map(int, input().split(" ")))
    print(prefix[b] - prefix[a-1])
# print(arr)
# print(prefix)
    