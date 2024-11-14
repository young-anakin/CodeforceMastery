n, m = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
root = [ind for ind in range(n+1)]
size = [arr[ind] for ind in range(n)]
size = [0] + size
def find(x):
    if x == root[x]:
        return x
    root[x] = find(root[x])
    return root[x]
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if size[rootX] > size[rootY]:
            root[rootX] = rootY
            size[rootX] = size[rootY]
        else:
            root[rootY] = rootX
            size[rootY] = size[rootX]
# print(root, size)
for ind in range(m):
    a, b = list(map(int, input().split(" ")))
    find(a)
    find(b)
    union(a,b)

    print(root, size)
sm = 0
tot = set()
for ind in range(n+1):
    root[ind] = find(ind)
    if root[ind] not in tot:
        tot.add(root[ind])
        sm += size[ind]
print(sm)

