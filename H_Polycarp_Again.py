n, k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

avg = sum(arr)/k

if avg != int(avg):
    print("No")
else:
    # print(arr)
    cp = 0
    sm = 0
    ind = 0
    ans = []
    fl = True

    while ind < n:
        # print(ind, arr)
        sm += arr[ind]
        cp +=1

        if sm == avg:
            ans.append(cp)
            cp = 0
            sm = 0
        elif sm > avg:
            fl = False
            break
        ind +=1
    # print(ans)
    if sm != 0:
        # print('ds')
        if len(ans) == 0:
            ans.append(cp)
        else:
            fl = False
    if fl:
        print("Yes")
        print(*ans)
    else:
        print("No")
