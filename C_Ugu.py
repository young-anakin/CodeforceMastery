t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    # print(s)
    on = False
    cp = 0
    last = s[0]
    fl = True
    for ind in s:
        # if fl and ind == "0":
        #     last = "0"
        #     continue
        if fl and ind == "1":
            fl = False
            last = "1"
            continue
        else:
            if last == "1" and ind == "0":
                cp +=1
                last = "0"
            elif last == "0" and ind == "1":
                cp +=1
                last = "1"
    
    print(cp)