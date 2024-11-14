t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    mx = max(arr)
    ans = []
    for _ in range(m):
        # print(mx)
        arr = list(map(str, input().split(" ")))
        # print(arr)
        a, b, c = arr[0], int(arr[1]), int(arr[2])
        # print(a,b,c)
        # print(b, mx, c)
        if b <= mx and c >= mx:
            if a == "+": 
                mx +=1
                ans.append(mx)
            else:
                mx -=1
                ans.append(mx)
        else:
            # print('a')
            ans.append(mx)
    print(*ans)