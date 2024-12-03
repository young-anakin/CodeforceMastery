t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    oneUp, twoUp = 0,0
    oneDown, twoDown = 0,0

    cp = 0
    cp += arr.count(3)
    cp += arr.count(1)

    print(cp)