t = int(input())
import bisect
for x in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    if n == 1:
        print(1)
    elif n%2 == 0:
        mx = -1 * float("inf")
        for ind in range(1, n,2):
            mx = max(arr[ind] - arr[ind-1], mx)
        print(mx)
    else:
        ss = set(arr)
        mn = float("inf")
        for ind in range(n):
            mx = 0
            if ind %2 == 0:
                # print("Level", ind)
                # print("first")
                fl = True
                for j in range(1, ind):
                    if fl:
                        mx = max(mx, arr[j] - arr[j-1])
                        # print("f", arr[j], arr[j-1])
 
                        fl = False
                    else:
                        fl = True
                # print("second")
                fl = True
                for j in range(ind+2, n):
                        # print("ka", j)
                    if fl:
                        mx = max(mx, arr[j] - arr[j-1])
                        # print(arr[j], arr[j-1])
 
                        fl = False
                    else:
                        fl = True
                # print("ans", mx)
                if arr[ind] +1  in ss and arr[ind]-1 in ss or arr[ind] == 0 or arr[ind] == 10**18:
                    continue
                else:
                    # print("yo")
                    mx = max(1, mx)
                    mn = min(mn, mx)  
                    # print("min", mn)           
 
        print(mn)
