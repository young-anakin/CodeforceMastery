n, a, b = list(map(int, input().split(" "))) 
arr = list(map(int, input().split(" ")))
i, j = 0, n-1
fl = True

tot = 0
while i < j:
    if arr[i] == 2 and arr[j] == 2:
        tot += min(a,b)*2
    elif arr[i] == 0 and arr[j] == 2:
        tot += a
    elif arr[i] == 2 and arr[j] == 0:
        tot += a
    elif arr[i] == 1 and arr[j] == 2:
        tot += b
    elif arr[i] == 2 and arr[j] == 1:
        tot += b
    elif arr[i] != 2 and arr[j] != 2:
        if arr[i] != arr[j]:
            fl = False
            break
    i+=1
    j -=1

if fl:
    if n%2 == 0:
        print(tot)
    else:
        # print(n//2)
        if arr[n//2] == 2:
            print(tot + min(a,b))
        else:
            print(tot)
else:
    print(-1)