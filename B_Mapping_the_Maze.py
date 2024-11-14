# prints all not yet visited vertices reachable from s 
from collections import defaultdict
def DFS(n,s, dd):            # prints all vertices in DFS manner from a given source.
    ans = []            # Initially mark all vertices as not visited 
    visited = set()
    fl = True

    # Create a stack for DFS 
    stack = []

    # Push the current source node. 
    stack.append(s) 

    while (len(stack)): 
        # Pop a vertex from stack and print it 
        s = stack[-1] 
        stack.pop()
 
        if (s not in visited): 
            # print(s,end=' ')
            visited.add(s)

        for node in dd[s]: 
            if (node not in visited):
                stack.append(node) 
            else:
                fl = False

    return fl

t = 1
from collections import defaultdict
sample = False
for _ in range(t):
 # number of nodes and edges
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for j in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
from collections import Counter
mx = max(graph.values(), key = lambda x: len(x))
# print(mx, graph)
one = 0
two = 0
multi = 0
# print(graph)
for key, values in graph.items():
    if len(values) == 2:
        two +=1
    elif len(values) == 1:
        one +=1
    else:
        multi +=1

if one == 2 and multi == 0:
    print("bus topology")
elif one == 0 and multi == 0 and two > 1:
    print("ring topology")
elif multi == 1 and two == 0 and one == n-1:
    print("star topology")
else:
    print("unknown topology")
# print(one, two, multi)
