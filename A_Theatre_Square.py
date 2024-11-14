a,b,c = list(map(int, input().split(" ")))

val = 0
import math
val += math.ceil(a/c)

val *= math.ceil(b/c)

print(val)
