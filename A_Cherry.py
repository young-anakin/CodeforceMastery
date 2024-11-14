t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr = list(set(arr))
    arr.sort()
    print(arr)
    if len(arr) != 1:
        print(arr[-1] * arr[-2])
    else:
        print(arr[-1] * arr[-1])