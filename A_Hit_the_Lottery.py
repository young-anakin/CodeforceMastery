n = int(input())

import math

ans = 0

sub = math.floor(n/100)
n -= sub * 100
ans += sub
sub = math.floor(n/20)
n -= sub * 20
ans += sub
sub = math.floor(n/10)
n -= sub * 10
ans += sub
sub = math.floor(n/5)
n -= sub * 5
ans += sub
sub = math.floor(n/1)
n -= sub * 1
ans += sub
# print(ans, n, sub)
print(ans)