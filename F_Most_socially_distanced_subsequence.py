t = int(input())
from collections import deque
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    # diff = deque()
    # for ind in range(len(arr)-1):
    #     diff.append(abs(arr[ind] - arr[ind+1]))
    
    ans = [arr[0]]
    if arr[0] > arr[1]:
        dec = True
    else:
        dec = False
    for ind in range(1, len(arr)-1):
        if dec:
            if arr[ind] > arr[ind+1]:
                pass
            else:
                dec = False
                ans.append(arr[ind])
        else:
            if arr[ind] < arr[ind+1]:
                pass
            else:
                dec = True
                ans.append(arr[ind])
    ans.append(arr[-1])
    print(len(ans))
    print(*ans)
