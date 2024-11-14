n, m = list(map(int, input().split(" ")))
from collections import defaultdict, deque
dd = defaultdict(list)
for _ in range(m):  
    a, b = list(map(int, input().split(" ")))
    dd[a].append(b)
    dd[b].append(a)


print(dd)
visited = set()
cp = 0
queue = deque()
for ind in range(1, n+1):
    if ind not in visited:
        queue.append(ind)
        ring = set()
        fl = True
        while queue:
            val = queue.popleft()
            visited.add(val)
            for ind in dd[val]:
                if ind not in visited:
                    if len(dd[val]) > 2 or len(dd[val]) < 2:
                        fl = False
                    queue.append(ind)
            if not fl:
                break
        if fl:
            cp +=1
        

