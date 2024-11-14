t = int(input())
from math import gcd
for ind in range(t):
    k = int(input())
    rest = 100 - k

    # while True:
    if k == 0 or rest == 0:
        print(1)
    else:
        ans = gcd(k, rest)
        while gcd(k, rest) != 1:
            k = k//ans
            rest = rest//ans
            ans = gcd(k, rest)
        print(rest + k)