from collections import defaultdict, deque

t = int(input())
graph = defaultdict(list)
for _ in range(t-1):
    a, b= list(map(int, input().split(" ")))
    # print(val)
    graph[a].append(b)
    graph[b].append(a)


init = list(map(int, input().split(" ")))
target = list(map(int, input().split(" ")))
queue = deque()
queue.append(1)
visited = set()
visited.add(1)
cp = 1
ans = []
while queue:
    val = queue.popleft()
    if init[val-1] != target[val-1]:
        cp +=1
    for ind in val:
        if ind not in visited:


print(graph)