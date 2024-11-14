a, b ,c, d = list(map(int, input().split(" ")))
mxa = 0
mxb = 0

mxa = max((3*a)/10, a - ((a/250) * c))
mxb = max((3*b)/10, b - ((b/250) * d))

if mxa == mxb:
    print("Tie")
elif mxa > mxb:
    print("Misha")
else:
    print("Vasya")