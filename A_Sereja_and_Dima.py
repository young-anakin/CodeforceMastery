n = int(input())
arr = list(map(int, input().split(" ")))
serge = 0
Dima = 0
l = 0 
r = n-1
while l <= r:
    if arr[l] >= arr[r]:
        serge += arr[l]
        l +=1
    else:
        serge += arr[r]
        r -=1
    if l > r:
        break
    if arr[l] >= arr[r]:
        Dima += arr[l]
        l +=1
    else:
        Dima += arr[r]
        r -=1
print(serge, Dima)


