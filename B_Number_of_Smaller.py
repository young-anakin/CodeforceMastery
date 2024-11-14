n, m = list(map(int, input().split(" ")))
arr1 = list(map(int, input().split(" ")))
arr2 = list(map(int, input().split(" ")))

a, b = 0, 0
ans = [0]
cp = 0
while a < n and b < m:
    if arr1[a] < arr2[b]:
        cp +=1
        a +=1
    
    else:
        ans.append(ans[-1] + cp)
        b+=1
        cp = 0
ans = ans[1:]

while len(ans) <= len(arr1):
    ans.append(len(arr1))
print(*ans)
