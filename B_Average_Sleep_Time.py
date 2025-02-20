n, k = list(map(int, input().split(" ")))
ans = list(map(int, input().split(" ")))

i, j = 0,k-1

cp = 0
arr = []
for x in range(k):
    cp += ans[x]

arr.append(cp)
j +=1
while j < n:
    # print(cp)
    cp += ans[j]
    cp -= ans[i]
    arr.append(cp)
    i +=1
    j +=1
# print(arr)
print(sum(arr)/len(arr))