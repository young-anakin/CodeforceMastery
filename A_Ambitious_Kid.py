n = int(input())

arr = list(map(int, input().split(" ")))
if 0 in arr:
    print(0)
else:
    odd = []
    even = []
    for ind in range(n):
        if arr[ind] < 0:
            odd.append(arr[ind])
        else:
            even.append(arr[ind])
    
    odd.sort()
    even.sort()

    if len(odd) == 0:
        print(even[0])
    elif len(even) == 0:
        print(abs(odd[-1]))
    else:


        print(min(even[0], abs(odd[-1])))