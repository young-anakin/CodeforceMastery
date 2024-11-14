n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))
    new = [abs(arr[i]) for i in range(sz)]
    print(sum(new))
