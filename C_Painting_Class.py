# prints all not yet visited vertices reachable from s 
def dfs(graph, s, color):            # prints all vertices in DFS manner from a given source.
                            # Initially mark all vertices as not visited 
    visited = [False for i in range(len(graph))] 
    # print(visited)
    # Create a stack for DFS 
    stack = []

    # Push the current source node. 
    stack.append((s, color[s-1])) 
    cp = 0
    while (len(stack)): 
        # Pop a vertex from stack and print it 
        s = stack[-1] 
        stack.pop()

        # Stack may contain same vertex twice. So 
        # we need to print the popped item only 
        # if it is not visited. 
        if (not visited[s[0]-1]): 
            # print(s,end=' ')
            visited[s[0]-1] = True

        # Get all adjacent vertices of the popped vertex s 
        # If a adjacent has not been visited, then push it 
        # to the stack. 
        for node in graph[s[0]]: 
            if (not visited[node-1]): 
                if color[node-1] != s[1]:
                    cp +=1
                stack.append((node, color[node-1])) 

        # print(stack)
    return cp+1

n = int(input())
from collections import defaultdict, deque
graph = defaultdict(list)
arr1 = list(map(int, input().split(" ")))
color = list(map(int, input().split(" ")))
for key, ind in enumerate(arr1):
    graph[key+2].append((ind ))
    graph[ind].append((key+2))

# print(graph)
print(dfs(graph, 1, color))
# queue = deque()
# visited = set()
# cp = 0
# queue.append((1, color[0]))
# while queue:
#     node = queue.popleft()
#     for val in graph[node[0]]:
#         if val not in visited:
#             visited.add(val)
#             if color[val-1] != node[1]:
#                 cp +=1
#             queue.append((val ,color[val-1]))
# print(cp)
# print(graph)