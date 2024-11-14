a, b = list(map(int, input().split(" ")))
if b %a != 0:
    print(-1)
elif b == a:
    print(0)
else:
    fl = True
    ans = b // a
    cp = 0
    while ans != 1:
        if ans %2 == 0:
            cp +=1
            ans = ans//2
        elif ans %3 == 0:
            cp +=1
            ans = ans//3
        else:
            fl = False
            # print(-1)
            break
    if fl:
        print(cp)
    else:
        print(-1)