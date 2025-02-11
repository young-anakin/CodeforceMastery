t = int(input())
for _ in range(t):
    s = input()
    fl = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            fl = True
            break

    if fl:
        print(1)
    else:
        print(len(s))
