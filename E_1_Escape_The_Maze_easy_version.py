n = int(input())
from collections import defaultdict, deque
for _ in range(n):
    space = input()
    graph = defaultdict(list)
    n, m = list(map(int, input().split(" ")))
    friends = list(map(int, input().split(" ")))
    endNodes = set()
    visited = set(friend for friend in friends)
    for ind in range(n-1):
        a, b = list(map(int, input().split(" ")))
        graph[a].append(b)
        graph[b].append(a)
    
    queue = deque((friend, 1) for friend in friends)
    for key, values in graph.items():
        if len(values) == 1:
            endNodes.add(key)
            # queue.append(key)
    queue.append((1, -1))
    ans = set()
    fin = False
    while queue:
        node = queue.popleft()
        fl = True
        for val in graph[node[0]]:
            if val not in visited:
                visited.add(val)
                queue.append((val, node[1]))
                if val in endNodes:
                    if node[1] == -1:
                        fl = False
                        break

        if not(fl):
            fin = True
            break
    if fin:
        print("YES")
    else:
        print("NO")
