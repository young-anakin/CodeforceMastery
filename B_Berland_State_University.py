t = int(input())
import math
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
 
    cp = 0
 
    for ind in arr:
        if ind == 1:
            cp +=1
 
    
    if n <= cp:
        x = 0
        count = 0
        ind = 0
        fl = False
        while count != n:
            if arr[ind] == 1:
                count +=1
                x +=1
                fl = True
                ind +=1
                continue
            else:
                if fl:
                    # print(ind)
                    x +=1
            ind +=1
        print(x)
    else:
        time = (n -1)// (cp)
        tott = math.ceil((n) /cp)
        # print("ka", math.ceil((n) /cp))


        first_week = 0
        mid_week = 0
        last_week = 0

        first_week = 7 - arr.index(1)
        # print(first_week)
        mid_week = 7 * (tott-2)
        # print(mid_week)
        cp = 0
        ind = 0
        print(last_week , mid_week , first_week, n)

        while first_week + mid_week + cp < n:
            print("kda")
            if arr[ind] == 1:
                cp +=1
            ind +=1
            last_week +=1

        print("lst", last_week)
        # last_week = arr.index(1)+1

        print(last_week + mid_week + first_week)

        # emikenes = 0
        # for ind in range(len(arr)):
        #     if arr[ind] == 1:
        #         break
        #     emikenes +=1
        # rest = n % cp
        # first = 0
        # for ind, val in enumerate(arr):
        #     if val == 1:
        #         first = ind
        #         break
        # print("r", rest, n, cp)

        # cp = 0
        # ind = 0
        # count = 0
        # while cp < rest:
        #     if arr[ind] == 1:
        #         cp +=1
        #         count +=1
        #     else:
        #         count +=1
        #     ind +=1
        # ans = time * 7
        # # print(first)
        # print(ans, count, first, emikenes)
        # print((ans + count + first) - emikenes)