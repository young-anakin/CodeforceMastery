from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    queue = deque()
    for val in arr:
        if len(queue) == 0:
            queue.append(val)
        else:
            if val > queue[0]:
                queue.append(val)
            else:
                queue.appendleft(val)
    
    print(*queue)