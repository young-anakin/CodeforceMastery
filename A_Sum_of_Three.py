t = int(input())
for _ in range(t):
    x = int(input())
    if x == 5 or x == 4 or x == 1 or x == 2 or x == 9 or x == 3 or x == 6:
        print("NO")
    elif x %3 == 0:
        print("YES")
        print(1, 4, x-5)
    else:
        a, b = 1, 2
        print("YES")
        print(a, b, x-3)

