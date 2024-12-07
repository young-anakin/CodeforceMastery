t = int(input())
for _ in range(t):
    n = input().strip()

    cp = [0, 0]
    sm = 0
    for c in n:
        if c == '2':
            cp[0] += 1
        elif c == '3':
            cp[1] += 1
        sm += int(c)

    if sm % 9 == 0:
        print("YES")
        continue

    left = 9 - (sm % 9)
    k = left + 9 if left % 2 else left

    while k >= 6 and cp[1]:
        k -= 6
        cp[1] -= 1

    while k > 0 and cp[0]:
        k -= 2
        cp[0] -= 1

    if k == 0:
        print("YES")
    else:
        print("NO")
