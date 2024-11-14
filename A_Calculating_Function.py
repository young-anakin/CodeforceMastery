n = int(input())
res = 0
even = int(n//2)
evenSum = even * (even+1)
if n%2 == 0:
    odd = even
else:
    odd = even+1
oddSum = odd**2
print(evenSum + (-oddSum))