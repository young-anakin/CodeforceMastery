n, m = list(map(int, input().split(" ")))
arr = []
for _ in range(n):
    i, j = list(map(int, input().split(" ")))
    arr.append(i*j)

ps = [0]
for i in arr:
    ps.append(ps[-1] + i)
import bisect
arr = list(map(int, input().split(" ")))
for i in arr:
    print(bisect.bisect_left(ps, i))