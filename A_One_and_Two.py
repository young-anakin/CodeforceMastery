t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))

    first = 1

    for ind in arr:
        first *= ind


    sm = 1
    fl = True
    for ind in range(len(arr)):
        sm *= arr[ind]

        if first/sm == sm:
            print(ind+1)
            fl = False
            break
    
    if fl:
        print(-1)

    # print(first)