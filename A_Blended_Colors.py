n = int(input())
for ind in range(n):
    size = int(input())
    arr = []
    for a in range(2):
        val = input()
        arr.append(val)
    flag = False
    for ind in range(2):
        for b in range(size):
            if (arr[0][b] == 'R' and (arr[1][b] == 'B' or arr[1][b] == "G")) or arr[1][b] == 'R' and (arr[0][b] == 'B' or arr[0][b] == "G"):
                flag = True
                break
        if flag == True:
            break
    
    if flag == False:
        print("YES")
    else:
        print("NO")