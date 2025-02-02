t = int(input())
for _ in range(t):
    b, c, h = list(map(int, input().split(" ")))
    cp = 0
    if b < 2:
        print(0)
    else:
        b -=2
        cp +=2
        while True:
            if c > 0 or h > 0:
                if c > 0:
                    cp +=1
                    c -=1
                elif h > 0:
                    cp +=1
                    h -=1
            else:
                break
            if b > 0:
                b -=1
                if c == 0 and h == 0:
                    cp -=1
                cp +=1
            else:
                break
        print(cp)
