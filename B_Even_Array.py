n = int(input())
for ind in range(n):
    s = int(input())
    arr = list(map(int, input().split(" ")))
    one = 0
    zero = 0
    for ind in range(s):
        if arr[ind] %2 != ind %2:
            if arr[ind] %2 == 0:
                zero +=1
            else:
                one +=1
    if one != zero:
        print(-1)
    else:
        print(one)

