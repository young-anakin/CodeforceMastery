test = int(input())

for _ in range(test):
    n = int(input())
    s = input()

    first  = 2
    ans = []

    for i in range(n):
        num = int(s[i])
        if ans:
            if int(ans[-1]) + int(s[i - 1]) == num + 1:
                ans.append("0")
            else:
                ans.append("1")
        else:
            ans.append("1")
    print("".join(ans))