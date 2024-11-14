n = int(input())
for ind in range(n):
    sz = int(input())
    val = input()

    a = 0
    b = sz-1
    cp = 0
    while a < b:
        if val[a] != val[b]:
            a +=1 
            b -=1
            cp +=2
        else:
            break
    print(sz - cp)
