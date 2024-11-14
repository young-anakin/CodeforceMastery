t = int(input())
for _ in range(t):
    fin = []
    for _ in range(9):
        arr = int(input())
        fin.append(str(arr))
    tot = []
    for ind in range(9):
        sub = []
        for j in range(9):
            sub.append(fin[ind][j])
        tot.append(sub)
          
    add = set()
    for ind in range(9):
        for j in range(9):
            if tot[ind][j] == "2":
                tot[ind][j] = "1"
    fin = []
    for ind in range(9):
        xx = "".join(tot[ind])
        print(xx)
    # print(tot)