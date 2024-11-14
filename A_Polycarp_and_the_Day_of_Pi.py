target = "314159265358979323846264338327"
n = int(input())
for ind in range(n):
    val = input()
    mx = 0
    j = 0
    for ind in range(len(val)):
        if val[ind] != target[ind]:
            break
        j +=1
    print(j)