t = int(input())
from math import factorial
# fx = factorial()
for _ in range(t):
    arr = []
    val = input()
    ans = 0
    cp = 0
    for ind in val:
        if arr:
            if arr[-1] != ind:
                if len(arr) ==1:
                    arr = []
                    arr.append(ind)
                else:
                    # print("Yooo")

                    cp += len(arr) - 1
                    ans += (factorial(len(arr)) % 998244353)
                    arr = []

                    arr.append(ind)
            else:
                arr.append(ind)
        else:
            arr.append(ind) 
    #     print(arr)
    # print(arr)
    
    if len(arr) > 1:
        # print("yooo")
        cp += len(arr) - 1
        ans += factorial(len(arr))
    
    if cp ==0 and ans == 0:
        ans +=1
    print(cp, ans)
    # print("-----")