n = int(input())
arr = list(map(int, input().split(" ")))


mx = 1
curr = 1

for ind in range(len(arr)-1):
    if arr[ind + 1] >= arr[ind]:
        curr +=1
        mx = max(curr, mx)
    else:
        curr = 1

print(mx)   