t = int(input())
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    tot = 0
    ss = set()
    a , b = list(map(int, input().split(" ")))
    for i in range(a, b+1):
        cp = 0
        if i %2 ==1 and i not in ss:
            ss.add(i)
            fl = True
            if i+1 <= b:
                cp +=1
                ss.add(i+1)
            else:
                fl = False
            if i+2 <= b:
                cp +=1
                ss.add(i+2)
            else:
                fl = False
        if cp == 2:
            tot +=1

    print(tot)
