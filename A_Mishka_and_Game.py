n = int(input())
mishCount = 0
chrisCount = 0
for ind in range(n):
    arr = list(map(int, input().split(" ")))
    if arr[0] > arr[1]:
        mishCount +=1
    elif arr[0] < arr[1]:
        chrisCount +=1

if mishCount > chrisCount:
    print("Mishka")
elif mishCount < chrisCount:
    print("Chris")
else:
    print("Friendship is magic!^^")

