n = int(input())
for ind in range(n):
    sz = int(input())
    ab = []
    for j in range(sz):
        sub  = input()
        ab.append(sub)
    for i in range(sz):
        fl = False
        for j in range(sz):
            if ab[i][j] == '1':
                if ab[i][j] == ab[i+1][j] == ab[i+1][j+1] == ab[i][j+1]:
                    print("SQUARE")
                else:
                    print("TRIANGLE")
                fl = True
                break 
        if fl == True:
            break