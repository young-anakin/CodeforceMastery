t = int(input())
from collections import defaultdict, deque
for _ in range(t):
    n = int(input())
    parent = list(map(int, input().split(" ")))
    color = input()
    graph = defaultdict(list)
    j = 2
    visited = set()
    black = defaultdict(int)
    white = defaultdict(int)
    for ind in parent:
        graph[j].append(ind)
        visited.add(ind)
        j +=1
    
    for ind in range(len(color)):
        if color[ind] == "W":
            white[ind+1] +=1
        else:
            black[ind+1] +=1

    
    # print(visited)

    queue = deque()
    # print(graph)
    # val, white, black
    for ind in range(1, n+1):
        if ind not in visited:
            queue.append((ind, white[ind], black[ind]))
    
    # print(queue)
    v = set()
    while queue:
        val, w, b = queue.popleft()
        for ind in graph[val]:
            white[ind] += white[val]
            black[ind] += black[val]
            if ind not in v:
                queue.append((ind, white[ind], black[ind]))
                v.add(ind)
            # v.add()
    
    cp = 0
    # print(graph)
    for ind in range(n):
        # print(black[ind+1], white[ind+1])
        if white[ind+1] == black[ind+1]:
            print(ind)
            cp +=1
    # print(white)
    # print(black)
            # if ind not in visited:
    print(cp)
    # print(graph)
