mod = pow(10, 9) + 7
import math
t = int(input())

tot = 2 ** t
# print(tot-2)
print(int(6 * pow(4, tot-2, mod)) % mod  )

