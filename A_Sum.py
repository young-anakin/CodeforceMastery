n = int(input())
for ind in range(n):
    arr = list(map(int, input().split(" ")))
    if arr[0] + arr[2] == arr[1]:
        print("YES")
        continue
    if arr[0] + arr[1] == arr[2]:
        print("YES")
        continue
    if arr[1] + arr[2] == arr[0]:
        print("YES")
        continue
    print("NO")