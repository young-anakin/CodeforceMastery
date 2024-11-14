n, r = list(map(int, input().split(" ")))
if n %2 == 0:
    if r <= n//2:
        print(1 + (2*(r-1)))
    else:
        r = r - n//2
        print(2 + (2*(r-1)))
else:
    if r <= n//2 + 1:
        print(1 + (2*(r-1)))
    else:
        r = r - n//2 +1
        print((2*(r-2)))