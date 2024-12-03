t = int(input())
for _ in range(t):
    arr = input()
    val = []
    sub = []
    for ind in arr:
        if ind == "=" or ind == ">" or ind == "<":
            val.append(sub)
            val.append(ind)
            sub = []
        else:
            sub.append(ind)
    
    val.append(sub)
    val[0] = "".join(val[0])
    val[2] = "".join(val[2])
    # print(val)


    if val[1] == "=":
        if int(val[0]) == int(val[2]):
            print("".join(val))
        else:
            if int(val[0]) > int(val[2]):
                print(str(val[0]) + ">" + str(val[2]))
            else:
                print(str(val[0]) + "<" + str(val[2]))
    elif val[1] == ">":
        if int(val[0]) > int(val[2]):
            print("".join(val))
        else:
            if int(val[0]) == int(val[2]):
                print(str(val[0]) + "=" + str(val[2]))
            else:
                print(str(val[0]) + "<" + str(val[2]))
    else:
        if int(val[0]) < int(val[2]):
            print("".join(val))
        else:
            if int(val[0]) == int(val[2]):
                print(str(val[0]) + "=" + str(val[2]))
            else:
                print(str(val[0]) + ">" + str(val[2]))
