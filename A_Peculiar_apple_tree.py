t = int(input())
from collections import defaultdict, deque
arr = list(map(int, input().split(" ")))
dd = defaultdict(int)
i = 2
stack = defaultdict(list)
for ind, val in enumerate(arr):
    dd[ind + 2] = val

graph = defaultdict(list)
level = defaultdict(int)

for ind, val in enumerate(arr):
    graph[val].append(ind+2)

queue = deque()
queue.append((1,1))
level[1] = 1
while queue:
    a, b = queue.popleft()
    for val in graph[a]:
        level[b+1] +=1
        queue.append((val, b+1))
    # queue.append()
# print("Graph", graph)
cp = 0
for key, val in level.items():
    if val %2 == 1:
        cp +=1
# print(level)
print(cp)

