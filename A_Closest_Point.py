t = int(input())
for _ in range(t):
    val = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort
    fl = True
    if len(arr) > 2:
        print("NO")
    else:
        for ind in range(val-1):
            if abs(arr[ind] - arr[ind+1]) == 1 or abs(arr[ind] - arr[ind+1]) == 0:
                print("NO")
                fl = False
                break
        if fl:
            print("YES")