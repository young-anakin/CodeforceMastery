t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    xx = list(sorted(arr))
    if xx == arr:
        print("YES")
    elif b == 1:
        print("NO")
    else:
        print("YES")