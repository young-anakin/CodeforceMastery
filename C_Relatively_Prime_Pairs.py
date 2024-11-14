a ,b = list(map(int, input().split(" ")))
if a == b:
    print("NO")
else:
    print("YES")
    # a = 0
    while a <= b:
        print(a, a+1)
        a +=2
    