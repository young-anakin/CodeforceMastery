t = int(input())
for _ in range(t):
    n = int(input())
    arr= list(map(int, input().split(" ")))
    if min(arr) == arr[0] or max(arr) == arr[-1]:
        print(max(arr) - min(arr))
    else:
        diff = -float("inf")
        # arr.extend(arr)
        for ind in range(len(arr)-1):
            diff = max(diff, arr[ind]-arr[ind+1])
        print(max(diff, max(arr) - arr[0], arr[-1] - min(arr) ))
