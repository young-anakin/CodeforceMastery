n = int(input())
for ind in range(n):
    sz = int(input())
    from collections import defaultdict
    dd = defaultdict(int)
    for j in range(sz):
        val = input()
        for c in range(len(val)):
            dd[val[c]] +=1
    fl = True
    # print(dd)
    tac = sz
    for key, values in dd.items():
        if values %sz != 0:
            fl = False
            print("NO")
            break

    if fl == True:
        print("YES") 
