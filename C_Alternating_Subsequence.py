t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))

    fl = 0
    if arr[0] > 0:
        fl = True
    else:
        fl = False
    sm = 0
    i = 0
    while i < n:
        if fl:
            mx = -1 * float("inf")
            while i< n and arr[i] >= 0:
                mx = max(mx, arr[i])
                i +=1
            # print(mx)
            sm += mx
            fl = False
        else:
            mx = -1 * float("inf")
            while i < n and arr[i] <= 0:
                mx = max(arr[i], mx)
                i +=1
            # print(mx)
            sm += mx
            fl = True
    print(sm)
        # if 
