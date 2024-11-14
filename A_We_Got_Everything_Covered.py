size = int(input())
for ind in range(size):
    n,k = list(map(int, input().split(" ")))
    first = ""
    for ind in range(n):
        s = ""
        a = 97
        for j in range(k):
            s += chr(a)
            a+=1
        first += s
    print(first)