m, s = list(map(int, input().split(" ")))
if (m != 1 and s == 0)  or (s > 9 * m):
    print("-1 -1")
elif m == 1 and s == 0:
    print("0 0")
else:
    both = []
    mx = []
    sm = 0
    for ind in range(m):
        mx.append(9)
        sm += 9
    fl = True
    # print(mx, sm)
    while fl:   
        for ind in range(m):
            degree = 0
            for j in range(9):
                if sm == s:
                    fl = False
                    break
                mx[ind] -=1
                sm -=1
                if sm == s:
                    fl = False
                    degree = j
                    break
            if not (fl):
                both.append("".join(map(str, mx[::-1])))
                break
    mx = []
    sm = 0
    for ind in range(m):
        mx.append(0)
        sm += 0
    mx[-1] = 1
    # fl = True
    sm +=1
    # print(mx)
    fl = True

    # if sm 
    if sm == s:
        fl = False
        both.append("".join(map(str, mx[::-1])))
    while fl:   
        for ind in range(m):
            for j in range(9):
                if sm == s:
                    fl = False
                    break
                mx[ind] +=1
                sm +=1
                # print(int("".join(map(str, mx))))
                if sm == s :
                    fl = False
                    break
            if not (fl):
                # both.append("".join(map(str, mx)))
                both.append("".join(map(str, mx[::-1])))

                break
    both.reverse()
    print(*both)
        