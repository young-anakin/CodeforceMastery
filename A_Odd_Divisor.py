n = int(input())
for ind in range(n):
    val = int(input())
    fl = True
    while val != 1:
        if val %2 != 0:
            fl = False
            break
        val = val/2
    if fl:
        print("NO")
    else:
        print("YES")