t = int(input())
for _ in range(t):
    n = int(input())
    val = input()
    alph = "abcdefghijklmnopqrstuvwxyz"
    mx = float("inf")
    for i in alph:
        cp = 0
        x, y = 0, n-1

        while x < y:
            if val[x] != val[y]:
                if val[x] != i and val[y] != i:
                    break
                elif val[x] == i:
                    x +=1
                    cp +=1
                else:
                    y -=1
                    cp +=1
            else:
                x +=1
                y-=1
        
        if y <= x:
            mx = min(mx, cp)
    if mx == float("inf"):
        print(-1)
        continue
    print(mx)
