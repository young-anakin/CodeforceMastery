t = int(input())
for _ in range(t):
    n = int(input())
    x = input()
    # print(x)
    val = x.find('8')
    if val == -1:
        print("NO")
    else:
        # print(n-val)
        if abs(n-val) >= 11:
            print("YES")
        else:
            print("NO")
    # print(val)