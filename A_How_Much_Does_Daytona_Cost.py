n = int(input())
for ind in range(n):
    m, k = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))

    if k in arr:
        print("YES")
    else:
        print("NO")