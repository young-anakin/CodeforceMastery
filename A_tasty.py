n, t = list(map(int, input().split(" ")))
arr = [0 for ind in range(t)]
i = 0
while n != 0:
    arr[i] +=1
    i +=1
    if i > (t-1):
        i = 0
    n -=1

print(*arr)