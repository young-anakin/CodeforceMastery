t = int(input())
for _ in range(t):
    x, y, a, b = list(map(int, input().split(" ")))

    if (y-x) % (a+b) == 0:
        print(abs(x-y)//(a+b))
    else:
        print(-1)
    