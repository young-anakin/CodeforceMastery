t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split(" ")))
    if abs(a-b) == 1:
        print(-1)
        continue
    circle = abs(b-a)-1
    tot = max(a,b) + circle
    # print("tot", tot)
    if c > tot:
        print(-1)
    else:
        if c > max(a,b):
            print(c-abs(a-b))
        else:
            print(c+abs(a-b))