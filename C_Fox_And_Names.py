n = int(input())
arr = []
from collections import defaultdict, deque
graph = defaultdict(list)
dependencies = defaultdict(int)
al = "abcdefghijklmnopqrstuvwxyz"
for _ in range(n):
    val = input()
    arr.append(val)
fl = True
for ind in range(0, len(arr)-1):
    a, b = arr[ind], arr[ind+1]
    if a[0] != b[0]:
        graph[a[0]].append(b[0])
        dependencies[b[0]] +=1
    else:
        for j in range(min(len(a), len(b))):
            if a[j] != b[j]:
                graph[a[j]].append(b[j])
                dependencies[b[j]] +=1
                break
for ind in graph:
    if len(graph[ind]) > 1:
        fl = False
# print(graph)
queue = deque()
extra = deque()
for ind in range(len(al)):
    if dependencies[al[ind]] == 0:
        queue.append(al[ind])
# print(queue)
if not fl:
    print("Impossible")
else:
    fin = ""
    while queue:
        val = queue.popleft()
        while extra and extra[-1][0] < val[-1]:
            new = extra.popleft()
            fin += new
            for j in graph[new]:
                extra.append(j)
        for ind in graph[val]:
            dependencies[ind] -=1
            if dependencies[ind] == 0:
                extra.append(ind)

        fin += val
    while extra:
        new = extra.popleft()
        fin += new
        for j in graph[new]:
            extra.append(j)
        # for ind in range(len(extra))
    # print(extra)
    if len(fin) != 26:
        print("Impossible")
    else:
        print("".join(fin))
