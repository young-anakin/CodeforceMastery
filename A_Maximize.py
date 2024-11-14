t = int(input())
import math
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
for _ in range(t):
    x = int(input())
    if is_prime(x):
        print(x-1)
    else:
        mx = 0
        ans = 0
        for i in range(2, x):
            if math.gcd(i, x) + i > mx:
                ans = i
                mx = math.gcd(i, x) + i
        print(ans)
