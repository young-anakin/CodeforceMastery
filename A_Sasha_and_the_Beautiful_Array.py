n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))

    arr.sort()
    sm = 0
    # 1 2 3 
    for j in range(len(arr)-1):
        sm += abs(arr[j] - arr[j+1])
    
    print(sm)