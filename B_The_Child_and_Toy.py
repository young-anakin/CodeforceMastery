n, m = list(map(int, input().split(" ")))
from collections import defaultdict
arr = list(map(int, input().split(" ")))
sm = 0
for _ in range(m):
    x, y = list(map(int, input().split(" ")))
    sm += min(arr[x-1], arr[y-1])

print(sm)
