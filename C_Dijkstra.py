n, m = list(map(int, input().split(" ")))
from collections import defaultdict
import heapq
dd = defaultdict(list)
visited = set()
for _ in range(m):
    a, b , w = list(map(int, input().split(" ")))
    dd[a].append((w,b))
    dd[b].append((w,a))

heap = []
ans = []
distances = defaultdict(int)

parent = defaultdict(int)
for val in range(n+1):
    distances[val] = float("inf")
heap.append((0, 1))
while heap:
    weight, node = heapq.heappop(heap)

    if node  in visited:
        continue

    visited.add(node)

    for w, val in dd[node]:
        nWeight = w + weight
        if nWeight < distances[val]:
            distances[val] = nWeight
            heapq.heappush(heap, (nWeight, val))
            parent[val] = node



parent[1] = 1
ans = []
i = n
while parent[i] != i:
    ans.append(i)
    i = parent[i]

ans.append(1)
ans = ans[::-1]
# print(parent)
if parent[n] == 0:
    print(-1)
else:
    print(*ans)  