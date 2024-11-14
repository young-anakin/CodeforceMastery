t = int(input())
for _ in range(t):

    even = False
    val = input()
    for i in val:
        if int(i) % 2 == 0:
            even = True

    if not even:
        print(-1)
    else:
        if int(val[-1]) %2 == 0:
            print(0)
        elif int(val[0]) %2 == 0:
            print(1)
        else:
            print(2)