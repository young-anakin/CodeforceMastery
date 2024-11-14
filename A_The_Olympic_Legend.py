n = int(input())
for i in range(n):
    arr = list(map(int, input().split(" ")))
    count = 0
    maxx = arr[0]
    for a in range(4):
        if arr[a] > maxx:
            count +=1
    print(count)
