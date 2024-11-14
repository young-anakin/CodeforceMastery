n = int(input())
ans = list(map(int ,input().split(" ")))
# print(ans)
arr = []
for i in range(n-1):
    arr.append(ans[i] + ans[i+1])

arr.append(ans[-1])
print(*arr)
