t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    # we divide by 2k to find the cycle closest to 0 ( to find earliest times when light is on)
    tk = 2 * k
    sub = []
    for ind in arr:
        earliest = ind%tk
        sub.append([earliest, earliest + k-1])
    
    check = [-float("inf"), float("inf")]
    # print(sub)
    for i in range(len(sub)):
        first, second = sub[i][0], sub[i][1]
        # if first < k:
        #     first += k-1
        #     second += k-1
        check[0] = max(check[0], first)
        check[1] = min(check[1], second)

    if check[0] > check[1]:
        # print(check)
        check = [-float("inf"), float("inf")]
        r = float("-inf")
        for ind in range(len(sub)):
            cur =  arr[ind] - arr[ind]%tk
            if sub[ind][0] < k:
                sub[ind][0] += tk
                sub[ind][1] += tk
                cur -= tk
            r = max(cur, r)
        for i in range(len(sub)):
            first, second = sub[i][0], sub[i][1]
            check[0] = max(check[0], first)
            check[1] = min(check[1], second)
        # print(check)
        if check[0] > check[1]:
            print(-1)
        else:
            # if check[0] < max(arr):
            # r = (max(arr) - max(arr)%tk)
            # print("blah", check[0])
            print(check[0]  + r)
            #     continue
            # print(check[0])           
    else:
    # if check[0] < max(arr):
        r = (max(arr) - max(arr)%tk)
            # print("blah", check[0])
            # print(check[0]  +r)
            # continue
        print(check[0] + r)
        # print(check)