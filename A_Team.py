def Team(val):
    count = 0
    for a in range(0, 3):
        if val[a] == 1:
            count +=1
    # print(count)
    if count >=2:
        return 1
    return 0
    

x = int(input())
fin = 0
for a in range(0, x):
    
    val = list(map(int, input().split()))
    fin += Team(val)
print(fin)