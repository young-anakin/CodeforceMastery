t = int(input())
from collections import defaultdict, deque
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split(" ")))
    dd = defaultdict(int)
    for i, val in enumerate(arr):
        dd[i+1] = val

    queue = deque()
    ans = []
    for ind in range(n):
        visited = set()
        queue.append(ind+1)
        cp = 0
        while queue:
            val = queue.popleft()
            if val not in visited:
                cp +=1
                visited.add(val)
                queue.append(dd[val])
            else:
                break
        ans.append(cp)
    print(*ans)