t = int(input())
for _ in range(t):
    n, m , k = list(map(int, input().split(" ")))
    a = list(input())
    b = list(input())
    a.sort()
    b.sort()

    a = a[::-1]
    b = b[::-1]
    ans = []
    acp = 0
    bcp = 0
    # print(a   , b)
    while len(a) != 0 and len(b)!= 0:
        # for ind in range(k):
        #     if len(a) != 0 and b!= len(b) != 0:
        #         if a[-1] < b[-1]:
        #             ans.append(a.pop())
        #         else:
        #             ans.append(b.pop())
        if (a[-1] < b[-1] and acp < k) or bcp >= k:
            acp += 1
            bcp = 0
            ans.append(a.pop())
        else:
            bcp +=1
            acp = 0
            ans.append(b.pop())
    
    # ans.extend(a)
    # ans.extend(b)
    print("".join(ans))
