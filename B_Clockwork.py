t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    fl = True
    for ind in range(len(arr)):
        left = ind
        right = len(arr) - (ind+1)

        # print(ind, arr[ind], left, right)
        if arr[ind] <= 2 * left or arr[ind] <= 2 * right:
            fl = False
            break
    
    if fl:
        print("YES")
    else:
        print("NO")

