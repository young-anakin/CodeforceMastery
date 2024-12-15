t = int(input())
for _ in range(t):
    val = input()
    ans = ""
    for ind in val:
        if ind == "q":
            ans += "p"
        elif ind == "p":
            ans += "q"
        else:
            ans += ind
    print(ans[::-1])