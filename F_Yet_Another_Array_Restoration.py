t = int(input())
def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # To avoid adding the square root twice if n is a perfect square
                factors.append(n // i)
    return sorted(factors)

for _ in range(t):
    n, b, c = list(map(int, input().split(" ")))
    diff = abs(b-c)
    fin = 0
    arr = []
    mnMax = [float("inf"), -1]
    ans = find_factors(diff)
    # print(ans)
    res = []
    for i in ans:
        count = (diff//i) + 1
        if count <= n:
            tmp = n
            tmp -= count
            tmp -= (b-1)//i

            if tmp <= 0:
                mnMax[0], mnMax[1] = c, i
                break
            else:
                r = c + i * tmp
                if r < mnMax[0]:
                    mnMax[0], mnMax[1] = r, i
    
    ans = [mnMax[0]]
    n -=1
    while n > 0:
        ans.append(ans[-1] - mnMax[1])
        n -=1

    # print(mnMax)
    print(*ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for ind in ans:
    #     sub = ind * a
    #     ans = []
    #     if sub > c:
    #         while sub > 0:
    #             ans.append(sub)
    #             sub -= ind
    #     print("ans", ans)
        