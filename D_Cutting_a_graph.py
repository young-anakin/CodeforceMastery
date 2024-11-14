n, m, t = list(map(int, input().split(" ")))
from collections import defaultdict
graph = defaultdict(list)
root = [i for i in range(n+1)]
size = [1] * (n+1)
edges = []
def find(x):
    while x != root[x]:
        root[x] = root[root[x]]
        x = root[x]
    return x
def union( x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if size[rootX] > size[rootY]:
            root[rootY] = rootX
            size[rootX] += size[rootY]
        else:
            root[rootX] = rootY
            size[rootY] += size[rootX]
def areRelated(x, y):
    # print(x, y)
    return find(x) == find(y)
for _ in range(m):
    val = list(map(int, input().split(" ")))
    edges.append(val)

op = []
for _ in range(t):
    val = list(map(str, input().split(" ")))
    op.append(val)
# print(root, size)
op = op[::-1]
ans = []
for val in op:
    if val[0] == 'ask':
        if areRelated(int(val[1]), int(val[2])):
            ans.append("YES")
        else:
            ans.append("NO")
    else:
        union(int(val[1]), int(val[2]))
ans = ans[::-1]
for val in ans:
    print(val)