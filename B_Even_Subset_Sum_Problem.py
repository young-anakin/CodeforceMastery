t = int(input())
from collections import defaultdict
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))

    ans = []
    even = 0
    evenHash  = 0
    oddHash = -1
    prefix = [0]
    for ind in range(len(arr)):
        prefix.append(prefix[-1] + arr[ind])
    
    for ind in range(len(arr)):
        if arr[ind] % 2 == 0:
            ans.append(ind+1)
            break
    if len(ans) > 0:
        print(1)
        print(*ans)
        continue

    # print(prefix)
    fl = True
    for ind in range(1, len(prefix)):
        if prefix[ind] %2 == 1:
            if oddHash == -1:
                oddHash = ind
                continue
            else:
                for i in range(oddHash, ind):
                    ans.append(i+1)
                    fl  = False
        else:
            for j in range(evenHash, ind):
                ans.append(j+1)
            fl = False
            break
            

    if fl:
        print(-1)
    else:
        print(len(ans))
        print(*ans)

    # print(ans)


