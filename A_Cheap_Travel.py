n, m, a, b = list(map(int, input().split(" ")))
first = (n//m * b) + min((n%m) * a, b)
second = a*n
if m*a <= b:
    print(n*a)
else:
    print(first)