t = int(input())
from collections import defaultdict
for _ in range(t):
    n = int(input())
    stack = []
    arr = list(map(int, input().split(" ")))
    memo = [0]*n
    # print(arr)
    for ind in range(len(arr)):
        if ind == 0:
            # print("yaaa", arr[ind], ind)

            memo[ind] = arr[ind]
            # print(memo)
        elif ind == 1:
            memo[ind] = arr[ind]
        
        else:
            memo[ind] = max(arr[ind] + memo[ind-2], arr[ind], memo[ind-2])
    
    # print(memo)
    print(max(memo))

