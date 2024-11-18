t = int(input())
import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True  # 2 and 3 are prime numbers
    if num % 2 == 0 or num % 3 == 0:
        return False  # Eliminate multiples of 2 and 3
    
    # Check divisors from 5 to sqrt(num) with a step of 6 (i.e., 6k ± 1)
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    
    return True
for _ in range(t):
    n = int(input())
    # if n%2 == 0:
    even = []
    odd = []

    for ind in range(1,n+1):
        if ind %2 == 0:
            even.append(ind)
        else:
            odd.append(ind)
    ans = []
    fl = False
    # print(even, odd)
    for ind in range(len(odd)):
        if is_prime(even[-1] + odd[ind]):
            continue
        else:
            odd[0], odd[ind] = odd[ind] , odd[0]
            fl = True
            break
    
    if not fl:
        print(-1)
    else:
    # for ind in range(n//2):
        ans.extend(even)
        ans.extend(odd)


        print(*ans)
        
