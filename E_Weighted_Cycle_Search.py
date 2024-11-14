t = int(input())
import heapq
from collections import defaultdict


for _ in range(t):
    heap = []
    n, m = list(map(int, input().split(" ")))
    root = [i for i in range(n+1)]
    size = [1] * (n+1)
    graph = defaultdict(list)
    small = [float('inf') for _ in range(n+1)]
    def find(x):
        while x != root[x]:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def union( x, y, w):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if size[rootX] > size[rootY]:
                root[rootY] = rootX
                size[rootX] += size[rootY]
                small[rootX] = min(small[rootX], w)
            else:
                root[rootX] = rootY
                size[rootY] += size[rootX]
                small[rootY] = min(small[rootY], w)
    def areRelated(x, y):
        return find(x) == find(y)
    arr = []
    for _ in range(m):
        u, v, w = list(map(int, input().split(" ")))
        arr.append((u, v, w))
        heap.append((w, u, v))
        graph[u].append(v)
        heap.sort(reverse= True)
    # print(heap)
    ans = []

    for i in heap:
        if not areRelated(i[1], i[2]):
            union(i[1], i[2], i[0])
        else:
            if len(ans) == 0:
                ans.append([i[0], i[1], i[2]])
            else:
                if ans[0][0] > i[0]:
                    # print(ans, i[0])
                    ans.pop()
                    ans.append([i[0], i[1], i[2]])
    print( ans)