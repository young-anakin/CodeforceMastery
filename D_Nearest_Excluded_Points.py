t = int(input())
from collections import defaultdict, deque
graph = defaultdict(list)
dir = [(1,0), (0, 1), (-1,0), (0,-1)]
visited = set()
li = list()
for _ in range(t):
    a, b = list(map(int, input().split(" ")))
    visited.add((a,b))
    li.append((a,b))
# print(visited)
def bfs(val):
    queue = deque()
    queue.append(val)
    ans = (0,0)
    fl = True
    tmp  = set()
    while fl:
        val = queue.popleft()
        for d in dir:
            ans = (val[0] + d[0], val[1] + d[1])
            # print(ans, ans in visited)
            if ans not in visited:
                fl = False
                break
            elif ans not in tmp:
                queue.append(ans)
                tmp.add(ans)
    return ans

for val in li:
    # print(val)
    print(*bfs(val))


