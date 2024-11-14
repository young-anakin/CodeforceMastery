n = int(input())
for _ in range(n):
    x, k = list(map(int, input().split(" ")))
    if x % k != 0:
        print(1)
        print(x)
    else:
        print(2)
        print(x-k-1, k+1)