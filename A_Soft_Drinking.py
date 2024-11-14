import math
arr = list(map(int, input().split(" ")))
n = arr[0]
n, k, l, c, d, p, nl, np = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6],arr[7]
ans = k * l
ans = ans// nl
limes = c*d
salt = p/np

print(int(min(salt,ans, limes)//n))
