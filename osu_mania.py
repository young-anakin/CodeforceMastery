t = int(input())
for _ in range(t):
    x = int(input())
    arr = []

    for _ in range(x):
        val = input()
        z = val.index('#')
        arr.append(z+1)
    print(*arr[::-1])