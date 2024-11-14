n = int(input())
li = [0,0,0]
for ind in range(n):
    val = list(map(int, input().split(" ")))
    li[0] += val[0]
    li[1] += val[1]
    li[2] += val[2]

if li == [0,0,0]:
    print("YES")
else:
    print("NO")


