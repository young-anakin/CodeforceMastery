def trial_division_simple(n) :
    factorization: list[int] = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factorization.append(d)
            n //= d
        d += 1
    if n > 1:
        factorization.append(n)
    
    ab = set(factorization)
    # print(ab)
    return len(ab) == 2
x = int(input())
cp = 0
for ind in range(1, x+1):
    if trial_division_simple(ind):
        # print(ind)
        cp +=1

# x = int(input())
if x == 1:
    print(0)
else:
    print(cp)