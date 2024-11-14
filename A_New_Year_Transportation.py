n, dest = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
i = 0
fl = False
while i < n-1:
    i += arr[i]
    if i == dest-1:
        print("YES")
        fl = True
        break

if not fl:
    print("NO")