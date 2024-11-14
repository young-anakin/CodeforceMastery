t = int(input())
from collections import defaultdict
for _ in range(t):
    n = int(input())
    graph = defaultdict(list)
    arr = list(map(int, input().split(" ")))
    first = 2
    for i in arr:
        graph[i].append(first)
        first +=1
    mx = 0
    print(graph)
    # for a, b in graph.items():
    #     mx = max(mx, len(b))
    # print(mx+1)