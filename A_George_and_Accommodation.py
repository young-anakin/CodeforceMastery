size = int(input())
count = 0
for i in range(0, size):
    val = list(map(int, input().split(' ')))
    if val[1] - val[0] < 2:
        pass
    else:
        count +=1
print(count)

    