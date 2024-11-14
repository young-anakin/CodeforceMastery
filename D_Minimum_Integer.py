even = ["0","2","4","6","8"]
odd = ['1','3','5','7','9']

x = int(input())
for ind in range(x):
    val = input()

    ev = []
    od = []
    for ind in range(len(val)):
        if val[ind] in even:
            ev.append(val[ind])
        else:
            od.append(val[ind])
    ans = []

    ev = ev[::-1]
    od = od[::-1]
    while len(od) > 0 and len(ev) > 0:
        if od[-1] > ev[-1]:
            ans.append(ev.pop())
        else:
            ans.append(od.pop())
    # for j in range(min(len(ev), len(od))):
    #     if ev[j] < od[j]:
    #         ans.append(ev[j])
    #         ans.append(od[j])
    #     else:
    #         ans.append(od[j])
    #         ans.append(ev[j])
    # print(ev, od)
    ev = ev[::-1]
    od = od[::-1]
    if len(ev) > len(od):
        for z in range(len(od), len(ev)):
            ans.append(ev[z])
        # ans.append(ev[len(od):])
    else:
        for z in range(len(ev), len(od)):
            ans.append(od[z])
    print("".join(map(str, ans)))
