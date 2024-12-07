n, m = list(map(int, input().split(" ")))
from collections import defaultdict, deque

graph = defaultdict(list)

arr = list(map(int, input().split(" ")))

for _ in range(n-1):
    a, b = list(map(int, input().split(" ")))
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
if arr[0] == 1:
    fl = True
else:
    fl = False
queue.append((1, arr[0], fl, 0))
visited = set()
cp = 0
# visited.add(1)
# print(arr[0])
while queue:
    val, curr, fl, mx = queue.popleft()
    # visited.add(val)

    print("mx", mx)

    if len(graph[val]) == 1:
        # print("mx", mx)
        # print("cancel", mx)
        if mx <= m:
            cp +=1
    if val  in visited:
        continue
    visited.add(1)

    for ind in graph[val]:
        if arr[ind-1] == 1:
            if fl:
                queue.append((ind, curr + 1, True, max(mx, curr + 1) ))
            else:
                queue.append((ind, curr + 1, True, max(mx, curr+1)))
        else:
            if fl:
                queue.append((ind, 0, False, max(mx, curr) ))
            else:
                queue.append((ind, 0, False, max(mx, curr)))
        
        visited.add(ind)
        
        
        
    

print(cp)
