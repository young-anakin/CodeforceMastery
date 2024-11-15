n, m = list(map(int, input().split(" ")))
from collections import defaultdict, deque
graph = defaultdict(list)

for _ in range(m):
    a, b = list(map(int, input().split(" ")))

    graph[a].append(b)
    graph[b].append(a)

cp = 1
visited = set()
queue = deque()
queue.append((1, -1))
parent = -1
repeated = False
# print(graph)
x = 0
while queue:
    val, parent = queue.popleft()
    for ind in graph[val]:
        if ind == parent:
            continue
        if ind not in visited:
            cp +=1
            queue.append((ind, val))
            visited.add(ind)
        else:
            repeated = True
            x +=1

# print(x)
import math
if cp == n and repeated and x <= math.ceil(n/2):
    print("FHTAGN!")
else:
    print("NO")
# print(repeated, cp)


# print(graph)