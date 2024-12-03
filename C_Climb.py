n, m = list(map(int, input().split(" ")))
if n < m :
    print(-1)

elif n == m:
    print(n)
else:
    arr = [2 for ind in range(n//2)]
    cp = len(arr)
    if n % 2 != 0:
        arr.append(1)
    
    tot = len(arr)

    fl = True
    if tot % m == 0:
        fl = False
    while tot % m != 0 and cp != 0:
        tot +=1
        cp -=1
        if tot % m == 0:
            fl = False
            break


    if fl:
        print(-1)
    else:
        print(tot)
        
