n = int(input())
for ind in range(n):
    val = int(input())
    # print(val)
    if val == 1 :
        print("NO")
    else:
        fl = False
        while val != 1:
            if val %2 != 0:
                # print("YES")
                fl = True
                break
            val = val//2
        if fl:
            print("YES")
        else:
            print("NO")