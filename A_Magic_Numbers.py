n = input()
fl = True
fCP = 0
if n[0] != '1':
    fl = False
for ind in n:
    if ind != "4" and ind != "1":
        fl = False
        break
    elif ind == "4":
        fCP +=1
        if fCP > 2:
            fl = False
    else:
        fCP = 0

if fl:
    print("YES")
else:
    print("NO")
