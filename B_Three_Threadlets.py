n = int(input())
for ind in range(n):
    arr = list(map(int, input().split(" ")))
    arr.sort()
    mn = min(arr)
    new = []
    i = 0
    steps = (arr[1]/mn)-1
    steps += (arr[2]/mn)-1
    if int(steps) != steps or steps  or if :
        print("NO")
    else:
        print("YES")
