t = int(input())
alph = []
for ind in range(26):
    alph.append(chr(ind + 97))

# print(alph)
for _ in range(t):
    val = input()
    ans = ""
    ans += val[0]
    fl = True
    for ind in range(1, len(val)):
        if val[ind] == val[ind-1] and fl:
            for j in range(len(alph)):
                if alph[j] != val[ind]:
                    ans += alph[j]
                    fl = False
                    break
            ans += val[ind]
        else:
            ans += val[ind]
    
    if fl:
        for ind in range(len(alph)):
            if ans[-1] != alph[ind]:
                ans += alph[ind]
                break
    print(ans)