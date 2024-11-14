t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    tmp = []
    for i, j in enumerate(arr):
        tmp.append((j , i))
    tmp.sort()
    # print(tmp)
    ps = [tmp[0]]
    for ind in tmp:
        ps.append((ps[-1][0] + ind, ps[-1][1]))
    # ps = ps[1:]
    ans = []
    ans.append(arr[-1])
    # for ind in range()
    print(ps)
    # for ind in range()