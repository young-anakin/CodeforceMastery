def gcd(a, b):
   if b == 0:
       return a
   return gcd(b, a % b)

a, b = list(map(int, input().split(" ")))
if a == b:
    print(a)
elif abs(b-a) == 1:
    print(gcd(a,b))
else:
    print(1)
# a, b = list(map(int, input().split(" ")))
# if a == b:
#     print(a)
# else:
#     print(1)