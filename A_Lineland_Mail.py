n = int(input())
arr = list(map(int, input().split(" ")))
mx = max(arr)
mn = min(arr)
for ind in range(n):
    if ind != 0 and ind != n-1:
        print(min(arr[ind] - arr[ind-1], arr[ind+1] - arr[ind] ), max(mx - arr[ind], arr[ind]-mn))
    elif ind == 0:
        print(arr[ind+1] - arr[ind], mx-mn)
    elif ind == n-1:
        print(arr[ind] - arr[ind-1], mx - mn)
    