
n = int(input())
for ind in range(n):
    a, b, l = list(map(int, input().split(" ")))
    cp = 0
    ans = set()
    # if a == b:
    #     for j in range(20):
    #         sub = pow(a, j)
    #         for x in range(1):
 
    #             sub2 = pow(b, x)
    #             if sub * sub2 > l:
    #                 break
    #             if l % (sub*sub2) == 0 and l/(sub * sub2) not in ans:
    #                 ans.add(l/(sub*sub2))
    #                 cp +=1
    # else:
    for j in range(20):
        sub = pow(a, j)
        for x in range(20):

            sub2 = pow(b, x)
            if (sub * sub2) > l:
                break
            if l % (sub*sub2) == 0 and l/(sub * sub2) not in ans:
                # print(l, sub*sub2)
                ans.add(l/(sub*sub2))
                cp +=1
    # print(ans)
    
    # print(ans)
 
    print(cp)