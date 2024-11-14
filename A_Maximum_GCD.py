import math

# Function to find the maximum gcd for a given n
def max_gcd(n):
    # Maximum gcd occurs between consecutive integers
    # So, we can return gcd(n-1, n) as the maximum gcd
    return math.gcd(n - 1, n)

# Input processing
t = int(input())
for _ in range(t):
    n = int(input())
    result = max_gcd(n)
    print(result)

