n = int(input())
arr = list(map(int, input().split(" ")))
minn = arr[0]
count = 0
maxx = arr[0]
for i in range(n):
    if arr[i] < minn:
        count +=1
        minn = arr[i]
    elif arr[i] > maxx:
        count +=1
        maxx = arr[i]
print(count)