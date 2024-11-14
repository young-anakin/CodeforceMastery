t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    arr = []
    for _ in range(n):
        sub = input()
        arr.append(sub)
    ans = []
    ind = 0
    while ind < n:
        t = 0
        sub = []
        while t < n:
            sub.append(arr[ind][t])
            t += k
        ind += k
        ans.append(sub)
    for ind in range(len(ans)):
        print("".join(ans[ind]))
    # print(ans)
    # print("89")