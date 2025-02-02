def prime_factors(n):
    factors = []
    divisor = 2

    while n >= 2:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

        # Optimization: Stop if divisor squared is greater than n
        if divisor * divisor > n and n > 1:
            factors.append(n)
            break

    return factors

# Example usage
# print(prime_factors(60))  # Output: [2, 2, 3, 5]
from collections import defaultdict, Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    primes = []
    for ind in arr:
        x = prime_factors(ind)
        # print(ind, x)
        primes.extend(prime_factors(ind))
    # print("----------")
    # print(primes)
    dd = Counter(primes)
    # print(dd)
    mx = -1
    fl = True
    for key, val in dd.items():
        if val % n != 0:
            fl = False
            break
    
    if fl:
        print("YES")
    else:
        print("NO")

