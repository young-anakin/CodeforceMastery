t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().split(" ")))
    mx = max(a+b, c+d)
    print(mx)