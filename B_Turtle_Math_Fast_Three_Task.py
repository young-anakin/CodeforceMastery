n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))

    sm = sum(arr)

    # print("ans : ", sm)
    if sm %3 == 0:
        print(0)
    elif (sm +1) % 3 == 0:
        print(1)
    else:
        fl = True
        for ind in range(len(arr)):
            if (sm - arr[ind]) % 3 == 0:
                print(1)
                fl = False
                break 
        if fl == True:
            print(2)