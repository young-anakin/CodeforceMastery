def determine_digits(n, d):
    ans = []

    ans.append(1)

    if n >= 3 or d % 3 == 0:
        ans.append(3)

    if d == 5:
        ans.append(5)

    if n >= 3 or (n == 2 and d == 7):
        ans.append(7)

    if n >= 6:
        ans.append(9)
    else:
        factorial = 1
        i = 2
        while i <= n:
            factorial *= i
            i += 1
        if (factorial * d) % 9 == 0:
            ans.append(9)

    return ans

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    ans = determine_digits(n, d)

    print(" ".join(map(str, ans)))
