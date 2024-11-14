n = input()

if int(n) >= 0:
    print(int(n))
else:
    b = len(n)
    a = 0
    vala = ""
    valb = ""
    while a < b:
        if a != b-1:
            vala += n[a]
        if a != b-2:
            valb += n[a]

        a +=1
    if vala >= valb:
        
        print(int(valb))
    else:
        print(int(vala))
        