n = int(input())
for ind in range(n):
    sz = int(input())
    val = input()
    rev = val[::-1]
    x=val.index('B')
    y = rev.index("B")
    print((len(val) - y) - x)