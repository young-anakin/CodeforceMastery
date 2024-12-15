t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    cp = 0
    for ind in range(n-1):
        if k == 0:
            continue
        else:
            while arr[ind] > 0 and k > 0:
                arr[ind] -=1
                k -=1
                cp +=1
    # print(arr)
    arr[-1] += cp
    print(*arr)


        