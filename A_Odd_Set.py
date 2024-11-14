n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))

    even = 0
    odd = 0
    for j in range(len(arr)):
        if arr[j] %2 == 0:
            even +=1
        else:
            odd +=1
    if even == odd:
        print("Yes")
    else:
        print("No")