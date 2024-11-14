n, m = list(map(int, input().split(" ")))
from collections import defaultdict
graph = defaultdict(list)
for _ in range(m):
    a, b, size  =list(map(int, input().split(" ")))
    graph[a].append((b, size))



print(graph)