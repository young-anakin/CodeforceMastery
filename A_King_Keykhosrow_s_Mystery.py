t = int(input())
import math
for _ in range(t):
    a,b = list(map(int, input().split(" ")))
    print(int(a*b / math.gcd(a,b)))