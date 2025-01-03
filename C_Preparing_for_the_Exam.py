t = int(input())
for _ in range(t):
    n, m , k = list(map(int, input().split(" ")))

    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    og = set()
    ss = set()
    for ind in b:
        og.add(ind)

    for ind in range(1, n+1):
        if ind not in og:
            ss.add(ind)

    ans = [] 
    for ind in range(len(a)):
        cp = 0
        if a[ind] in ss:
            cp +=1
        if len(ss) - cp == 0:
            ans.append(1)
        else:
            ans.append(0)
    
    # x = *ans
    result = "".join(map(str, ans))

    print(result)