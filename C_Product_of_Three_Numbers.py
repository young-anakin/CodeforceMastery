t = int(input())
def prime_factors(n):
    factors = []
    
    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors
for _ in range(t):
    n = int(input())
    factors = prime_factors(n)
    factors.sort()
    ss = set()
    curr = 1
    fl = False
    for ind in range(len(factors)):
        curr *= factors[ind]
        if len(ss) == 2:
            fl = True
            continue
        if curr not in ss:
            ss.add(curr)
            curr = 1
            # cp +=1
        # else:
        #     curr *= factors[ind]
    
    if fl:
        if curr not in ss:
            ss.add(curr)
    
    if len(ss) < 3:
        print("NO")
    else:
        arr = list(ss)
        arr.sort()
        print("YES")
        print(*arr)
    # print(ss)
    



    cp = 0

    # print(factors)

