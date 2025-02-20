t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    arr.sort(reverse= True)
    i, j = 0,0
    mx = 0
    # print(arr)
    sm = 0
    diff = 0
    for i in arr:
        diff += i -x
    diff = abs(diff)
    # print(diff)
    while j < n:
        sm += arr[j]
        # print(sm, sm // (j+1), x)
        if (sm // (j+1)) >= x:
            mx = max(mx, abs(j+1)) 
            j +=1
        else:
            break

    # print("======")
    print(mx)

