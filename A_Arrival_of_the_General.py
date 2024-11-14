n = int(input())
arr = list(map(int, input().split(" ")))
mx = -1
sm = 0
lr = 0
mn =  100000000000000
for ind in range(n):
    if arr[ind] > mx:
        lr = ind
        mx = arr[ind]
    if arr[ind] <= mn:
        mn = arr[ind]
        sm = ind
# print(lr, sm)
# if sm == n-1 and lr == 0:
#     print(0)
if sm > lr:
    print((n-1) - sm + lr - 0)
else:
    print(((n-1) - sm + lr - 0)-1)