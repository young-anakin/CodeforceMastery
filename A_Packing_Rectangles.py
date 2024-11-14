a, b , n = list(map(int, input().split(" ")))
l, r = 0, max(a,b) * n
import math
def prod(x):
    return math.floor(x/b) * math.floor(x/a) >= n
while l+1 <r :
    m = (l+r)//2
    if prod(m):
        r = m
    else:
        l = m
print(r)
