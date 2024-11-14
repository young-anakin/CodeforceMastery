t = int(input())
for _ in range(t):
    a, b, c ,n = list(map(int, input().split(" ")))
    # if a == b == c:
    #     print("Yes")
    mx = max(a,b,c)
    n -= mx - a
    n -= mx-b
    n -= mx-c
    # print(n)
    if n < 0:
        print("NO")
    else:
        if n%3 == 0 :
            print("YES")
        else:
            print("NO")