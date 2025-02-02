n, b , d = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
cp = 0
ans = 0
for i in range(n):
    if arr[i] > b:
        continue
    else:
        cp += arr[i]
    
    if cp > d:
        ans +=1
        cp = 0
    
print(ans)