n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
from collections import deque, defaultdict
dd = defaultdict(bool)
queue = deque()
for i in arr:
    if dd[i] == False:
        dd[i] = True
        if len(queue) == k:
            x = queue.pop()
            dd[x] = False
        else:
            pass
        queue.appendleft(i)   
    else:
        continue 
print(len(queue))
print(*queue)