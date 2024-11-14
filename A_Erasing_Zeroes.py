n = int(input())
for ind in range(n):
    val = input()
    cp = 0
    ans = 0
    check = False
    for j in range(len(val)):
        if val[j] == "1":
            ans += cp
            check = True
            cp = 0
        else:
            if check == True:
                cp +=1
    print(ans)