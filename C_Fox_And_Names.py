t = int(input())
alph = list()
for ind in range(26):
    alph.append(chr(ind + 97))

# print(alph)

i = 0
ans = ""
given = []
for ind in range(t):
    val = input()
    given.append(val[0])

cp = 0
ss = set()
ss.add(given[0])
fl = True
for ind in range(1, len(given)):
    if given[ind] not in ss:
        ss.add(given[ind])
        cp +=1 
    else:
        if given[ind] != given[ind-1]:
            fl = False
            break

if not fl:
    print("Impossible")
else:
    # for ind in range(len(alph)):
    #     if 
    ss2 = set()
    choose = []
    ans = ""
    for ind in given:
        if ind not in ss2:
            choose.append(ind)
            ss2.add(ind)
    
    choose = choose[::-1]
    # ss2 = set()
    for ind in alph:
        if ind not in ss:
            ans += ind
            ss2.add(ind)
        else:
            if choose[-1] == ind:
                choose = choose[::-1]
                ans += "".join(choose)
                break
    
    for ind in alph:
        if ind not in ss2:
            ans += ind
    print(ans)
