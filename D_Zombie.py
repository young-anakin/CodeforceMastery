n, m = list(map(int ,input().split(" ")))
from collections import defaultdict, deque
graph = defaultdict(list)
target = 0
fl = True
for _ in range(m):
    a, b = list(map(int, input().split(" ")))
    if fl:
        target = a
    fl = False
    graph[a].append(b)
    graph[b].append(a)


# for ind in range()
mx = 0
queue = deque()
# queue.append((target, 0))
visited = set()
visited.add(target)
# print(target)
fin = 0
mx = float("inf")
# print(graph)
for key, val in graph.items():
    if len(val) <= mx:
        mx = len(val)
        fin = key
# print(fin)
# while queue:
#     # print(queue)
#     val, xp = queue.popleft()
#     fin = val

#     for ind in graph[val]:
#         if ind not in visited:
#             queue.append((ind, xp+1))
#             visited.add(ind)

# print(fin)
visited = set()
visited.add(fin)
queue.append((fin, 0))
mn = 0
# print(queue)
while queue:
    # print(queue)
    val, xp = queue.popleft()
    # print(xp)
    mn = max(xp, mn )

    for ind in graph[val]:
        if ind not in visited:
            visited.add(ind)
            queue.append((ind, xp+1))


print(mn)
