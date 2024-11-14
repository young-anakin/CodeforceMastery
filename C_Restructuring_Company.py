n, q = list(map(int, input().split(" ")))
root = [i for i in range(n+1)]
size = [1] * (n+1)
mn = float("inf")
mx = -float("inf")
def find(x):
    while x != root[x]:
        root[x] = root[root[x]]
        x = root[x]
    return x
import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
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
for _ in range(q):
    a, b , c = get_ints()
    if a == 3:
        if areRelated(b, c):
            sys.stdout.write("YES" + "\n")
        else:
            sys.stdout.write("NO" + "\n")
    elif a == 2:
        for ind in range(b, c):
            if not areRelated(ind, ind+1):
                union(ind, ind+1)
    else:
        if not areRelated(b, c):
            union(b, c)
