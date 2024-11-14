n, x = list(map(int, input().split(" ")))
cp = 0
for ind in range(n):
    val = list(map(str, input().split(" ")))
    if val[0] == "+":
        x += int(val[-1])
    else:
        if x < int(val[-1]):
            cp +=1
            # print(ind, x)
            continue
        else:
            x -= int(val[-1])

print(x, cp)