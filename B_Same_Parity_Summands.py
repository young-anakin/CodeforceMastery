t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    if n%2 == 1:
        print("NO")
    elif k > n:
        print("NO")
    else:
        