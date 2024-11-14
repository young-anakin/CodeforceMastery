n = int(input())
for _ in range(n):
    a, b, c = list(map(int, input().split(" ")))
    first = a - c
    second = abs(b-c)

    if first > second:
        print(2)
    elif first < second:
        print(1)
    else:
        print(3)