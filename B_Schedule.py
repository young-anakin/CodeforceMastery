n = int(input())
arr = list(map(int, input().split(" ")))
cp = 0
fl = False
for ind in range(n):
    if fl == False:
        if arr[ind] == 1:
            fl = True
            cp +=1
        else:
            continue
    else:
        if arr[ind] == 1:
            cp +=1
        else:
            if ind + 1 == n:
                continue
            else:
                if arr[ind+1] == 0:
                    fl = False
                else:
                    cp +=1
print(cp)
            
