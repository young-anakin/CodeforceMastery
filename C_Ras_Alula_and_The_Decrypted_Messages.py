n = int(input())
for ind in range(n):
    normal, weird = list(map(int, input().split(" ")))
    first = input()
    second = input()

    a = 0
    b = weird

    # x = 0
    # y = 0
    sm1 = 0
    sm2 = 0
    # print("----")
    for ind in range(weird):
        # print(ord(first[ind]) - ord(second[ind]))
        sm1 += ord(first[ind]) 
        sm2 += ord(second[ind])
    print(sm2, sm1)
    if sm1 - sm2 == 0:
        print("YES")
    else:
        fl = False
        while b < normal:
            sm1 -= ord(first[a])
            sm1 += ord(first[b])
            print(sm1)
            if sm1 == sm2:
                fl = True
                break
            a +=1
            b+=1
        # print(normal)
        if fl:
            print("YES")
        else:
            print("NO")


