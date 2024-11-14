t = int(input())
for _ in range(t):

    val = int(input())
    if val < 3:
        print(1)
    elif val == 4:
        print(1)
    else:
        tmp = (val - (val//4)*4)
        # print(tmp)
        print(val//4 + tmp//2)