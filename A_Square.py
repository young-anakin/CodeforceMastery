t = int(input())
for _ in range(t):
    arr = []
    unique = []
    for _ in range(4):
        x, y = list(map(int, input().split(" ")))
        arr.append((x, y))
    arr.sort()

    print(abs(arr[0][1] - arr[1][1])  *  abs(arr[2][1] - arr[3][1]))