n = int(input())
for ind in range(n):
    size = int(input())
    first = input()
    second = input()
    third = input()
    flag = False
    for ind in range(size):
        if first[ind] != third[ind] and second[ind] != third[ind]:
            flag = True
            break
    if flag == True:
        print("YES")
    else:
        print("NO")
