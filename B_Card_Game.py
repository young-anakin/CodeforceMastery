t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().split(" ")))
    # if a > c and a > d and b > c and b > d:
    #     print(4)
    # elif a < c and b < c and a < d and b < d:
    #     print(0)
    # elif    
    cp = 0
    if a > c and b > d:
        cp +=1
    if a > d and b > c:
        cp +=1
    if b > c and a > d:
        cp +=1
    if b > d and a > c:
        cp +=1
    print(cp)