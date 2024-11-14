t = int(input())
for _ in range(t):
    n, a, b = list(map(int, input().split(" ")))
    str = []
    i = 0
    for _ in range(a):
        if i == b:
            i = 0
        str.append(chr(97 + i))
        i +=1
    str *= 2000
    str = str[0:n]
    print("".join(str))