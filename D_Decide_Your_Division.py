t = int(input())
for _ in range(t):
    val = int(input())
    if val == 1:
        print(0)
        continue
    cp = 0
    fl = True
    # print(val)
    while val != 1:
        if val%2 != 0 and val%3 != 0 and val%5 != 0:
            print(-1)
            fl = False
            break
        else:
            og = val
            if val%2 == 0:
                val = min(og, og//2)
            if val%3 == 0:
                val = min(og, (og*2)//3)
            if val%5 == 0:
                val = min(og, (og*4)//5)
        # print(val, "val" )
        cp +=1
    if fl:
        print(cp)