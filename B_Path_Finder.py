n = int(input())
from collections import defaultdict, deque
graph = defaultdict(list)
for ind in range(n-1):
    arr = list(map(int, input().split(" ")))
    graph[arr[0]].append((arr[1], arr[2]))
    graph[arr[1]].append((arr[0], arr[2]))

leaf = set()
for key, val in graph.items():
    if len(val) == 1:
        leaf.add(key)
visited = set()
queue = deque()
queue.append((0, 0))
final = set()
while queue:
    val = queue.popleft()
    for ind in graph[val[0]]:
        if ind not in visited:
            visited.add(ind)
            if ind[0] in leaf:
                final.add(ind[1]+val[1])
            queue.append((ind[0], ind[1]+val[1]))

print(max(final))
