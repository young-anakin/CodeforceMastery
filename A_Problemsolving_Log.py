dd = {}
for ind in range(26):
    dd[chr(ind+97)] = ind+1

n  = int(input())
for ind in range(n):
    sz = int(input())
    vl = input()
    for j in range(len(vl)):
        sz -= dd[vl[j].lower()]
        fl = True
        if sz == 0:
            print(j+1)
            fl = False
            break
        elif sz < 0:
            print(j)
            fl = False
            break
    if fl == True:
        print(j)
