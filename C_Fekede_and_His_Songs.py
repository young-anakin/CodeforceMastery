n, m = list(map(int, input().split(" ")))
arr = [0]
import bisect
for _ in range(n):
    a, b = list(map(int, input().split(" ")))
    arr.append(arr[-1] + a*b)

all = list(map(int, input().split(" ")))
# arr = [0]
# for _ in range(m):
#     val = input()
arr = arr[1:]
for ind in all:
    x = bisect.bisect_left(arr, ind)
    print(x+1)
# print(arr)

