n = int(input())
arr = [-1 for ind in range(n)]

def DFS(s, dd):            # prints all vertices in DFS manner from a given source.
                                # Initially mark all vertices as not visited 
        visited = set()
 
        # Create a stack for DFS 
        stack = []
 
        # Push the current source node. 
        stack.append(s) 
 
        while (len(stack)): 
            # Pop a vertex from stack and print it 
            s = stack[-1] 
            stack.pop()
 
            # Stack may contain same vertex twice. So 
            # we need to print the popped item only 
            # if it is not visited. 
            if (s not in visited): 
                print(s,end=' ')
                visited.add(s)
 
            # Get all adjacent vertices of the popped vertex s 
            # If a adjacent has not been visited, then push it 
            # to the stack. 
            for node in dd: 
                if (node not in visited): 
                    stack.append(node) 
            # print(visited)
        # return stack


# n = int(input())
t = 1

from collections import defaultdict, deque
graph = defaultdict(list)
for _ in range(n-1):
 # number of nodes and edges
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)
    # ans.append()
# print(graph)
color = [-1 for _ in range(n+1)]
val = [1,0]
dd = deque([1])
color[1] = 0
while dd:
     temp = dd.popleft()
     for i in graph[temp]:
        if color[i] == -1:
            color[i] = 1 - color[temp]
            dd.append(i)
            val[1-color[temp]] +=1

ans = 0
for ind in graph:
    tt = len(graph[ind])
    opp = 1 - color[ind]
    ans += abs(tt - val[opp])
    # print(tt, opp)
print(ans//2)
