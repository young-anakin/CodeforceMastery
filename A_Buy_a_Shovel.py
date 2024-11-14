n, m = list(map(int, input().split(" ")))
cp = n
while True:
    if (n-m) % 10 == 0 or n%10 == 0:
        break
    else:
        n += cp

print(n//cp)
