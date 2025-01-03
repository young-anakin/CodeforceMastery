import math

t = int(input())  # Number of test cases
results = []

for _ in range(t):
    n = int(input())  # Value of the coin
    if n <= 3:
        results.append(1)
    else:
        max_coins = 2 ** math.floor(math.log(n, 4))
        results.append(max_coins)

print("\n".join(map(str, results)))
