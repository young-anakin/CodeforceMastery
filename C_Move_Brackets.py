n = int(input())
for ind in range(n):
    sz = int(input())
    li = input()
    closed = 0
    opened = 0
    cp = 0
    for j in range(1, sz+1):
        if li[-j] == ")":
            closed +=1
        else:
            # print(closed, li[-j])
            if closed >= 1:
                closed -=1
        # print(closed)
    # print("----------")
    print(closed)
    # print(closed)
        