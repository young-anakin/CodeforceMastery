n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))

    odd = 0
    even = 0
    for ind in range(len(arr)):
        if arr[ind] %2 != 0:
            odd +=1 
        else:
            even +=1
    
    if odd %2 == 0:
        print("YES")
    else:
        print("NO")