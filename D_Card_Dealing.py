t = int(input())
for _ in range(t):
    n = int(input())
    turn = False
    a, b = 1,0
    i = 1
    while a + b < n:
        if turn:
            # print("hoa", i)
            i +=1
            if b + a + i <= n:
                a += i
                # print("alice", a)
            else:
                break
            i +=1
            if b + a+ i <= n:
                a +=i
                # print("alice", a)
            else:
                break
            # print("ua", a,b)
            turn = False
        else:
            i +=1
            if b + a + i <= n:
                b += i

                # print("bob", i, b)
            else:
                break
            i +=1
            if b + a+ i <= n:
                b +=i
                # print("bob", i, b)

            else:
                break
            turn = True
        # print(a, b, n)
    if a + b < n:
        if turn:
            a += n-(a+b)
        else:
            b += n- (a+b)
    print(a,b)