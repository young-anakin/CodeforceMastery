n = int(input())
arr = list(map(int, input().split(" ")))
mx = 0
stack = []
cp = 0
for ind in range(len(arr)-1):
    if arr[ind] < arr[ind+1]:
        cp +=1
    else:
        mx = max(cp+1, mx)
        cp = 0
mx = max(cp+1, mx)
print(mx)