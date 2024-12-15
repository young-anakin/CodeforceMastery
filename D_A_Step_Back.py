t = int(input())
for _ in range(t):
    n, k, z = list(map(int, input().split(" ")))

    arr = list(map(int, input().split(" ")))
    # print(arr)

    for ind in range(n):
        for j in range(z):
            