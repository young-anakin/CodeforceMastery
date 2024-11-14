t = int(input())
from collections import Counter
for _ in range(t):
    s = input()
    t = input()
    sarr = []
    same = 0
 
    for ind in range(len(s)):
        sarr.append(s[ind])
    cps = Counter(s)
    cpt = Counter(t)
    i = 0
    if True:
        for ind in range(len(t)):
            # print(t[ind])
            fl = False
            if i >= len(s):
                break
            if s[i] == t[ind]:
                # print(s[ind])
                i +=1
                fl = True
            else:
                while i < len(s):
                    # print(t[ind], s[i])
                    if s[i] == '?' or s[i] == t[ind]:
                        sarr[i] = t[ind]
                        fl = True
                        i +=1
                        break
                    i +=1
                
            if fl:
                same +=1
    if len(t) <= same:
        # print(same)
        for ind in range(len(sarr)):
            if sarr[ind] == "?":
                sarr[ind] = "a"
        val = "".join(sarr)
        print("YES")
        print(val)
    else:
        print("NO")
    # print(same)