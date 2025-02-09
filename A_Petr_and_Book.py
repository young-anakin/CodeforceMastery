t = int(input())
arr = list(map(int, input().split(" ")))
arr = arr * 1000
ans = 0
for ind in range(len(arr)):
    t -= arr[ind]
    if t <= 0:
        break

print((ind % 7) + 1)