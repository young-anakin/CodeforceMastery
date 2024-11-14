n, m = list(map(int, input().split(" ")))
from collections import defaultdict, deque
import heapq
graph = defaultdict(list)
dependency = defaultdict(int)
for ind in range(m):
    val = list(map(int, input().split(" ")))
    graph[val[0]].append(val[1])
    dependency[val[1]] +=1
ans = []
queue = []
for ind in range(1, n+1):
    if dependency[ind] == 0:
        heapq.heappush(queue, ind)
visited = set()
# print(graph, dependency, queue)
while queue:
    val = heapq.heappop(queue)
    # if val not in visited:
    ans.append(val)
    # visited.add(val)
    for ind in graph[val]:
        dependency[ind] -=1
        if dependency[ind] == 0:
            # if ind not in visited:
            #     ans.append(ind)
            #     visited.add(ind)
            heapq.heappush(queue, ind)
if len(ans) != n:
    print(-1)
else:
    print(*ans)