size = int(input())
for ind in range(size):
    val = list(map(int, input().split(" ")))
    ans = 1
    cp = 1
    check = val[0]-2
    if val[0] == 0 or val[0] == 1:
        print(1)
    else:
        while ans <= check:
            ans += val[1]
            cp += 1
        print(cp)
