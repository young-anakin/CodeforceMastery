n = int(input())
for ind in range(n):
    first, second = list(map(int, input().split(" ")))

    t = input()
    s = input()
    cp = 0
    fl = True
    for ind in range(26):
        if s in t:
            print(ind)
            fl = False
            break
        t += t


    if fl == True:
        print(-1)

    
