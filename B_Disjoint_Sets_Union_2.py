n, t = list(map(int, input().split(" ")))
root = [i for i in range(n+1)]
size = [1] * (n+1)
mx = [i for i in range(n+1)] 
mn = [i for i in range(n+1)]
from collections import defaultdict
dd = defaultdict(list)
for ind in range(1, n+1):
    dd[ind].append(ind)
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
            mn[rootX] = min(mn[rootX], mn[rootY])
            mx[rootX] = max(mx[rootX], mx[rootY])
        else:
            root[rootX] = rootY
            size[rootY] += size[rootX]
            mn[rootY] = min(mn[rootY], mn[rootX])
            mx[rootY] = max(mx[rootY], mx[rootX])
def areRelated(x, y):
    # print(x, y)
    return find(x) == find(y)
for _ in range(t):
    val = list(map(str, input().split(" ")))
    if "union" in val:
        union(int(val[1]), int(val[2]))
    else:
        val[1] = find(int(val[1]))
        # print(root)
        print(mn[val[1]], mx[val[1]], size[val[1]])
