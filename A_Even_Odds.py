# 1, 3, 5, 7, 9, 2, 4, 6, 8, 10

# 1, 3, 5, 7, 2, 4, 6
import math
li = list(map(int, input().split(" ")))

if li[1] <= math.ceil(li[0]/2):
    print(li[1] + li[1]-1)
else:
    x = li[1] - math.ceil(li[0]/2)
    print(x * 2)