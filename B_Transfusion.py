t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    sm = sum(arr)
    
    if sm % n != 0:
        print("NO")
        continue
    
    # print(arr)
    req = sm // n
    possible = True
    # print(req)
    for i in range(1, n - 1):
        # print(arr[i-1], arr[i+1])
        if arr[i - 1] == req:
            continue
        elif arr[i - 1] < req:
            diff = req - arr[i - 1]
            arr[i - 1] += diff
            arr[i + 1] -= diff
        else:
            diff = arr[i - 1] - req
            arr[i - 1] -= diff
            arr[i + 1] += diff
    
    for i in range(n):
        if arr[i] != req:
            possible = False
            break
    
    # print(possible)
    if possible:
        print("YES")
    else:
        print("NO")
