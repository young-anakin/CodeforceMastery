a, b = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
arr.sort()

luckiest = 0
unluckiest = 0

from collections import Counter

li = []
for ind in range(b):
    x = input()
    li.append(x)
cp = Counter(li)

new = []

for key, values in cp.items():
    new.append(values)

new.sort()
new = new[::-1]
for ind in range(len(new)):
    luckiest += arr[ind] * new[ind] 
# print(luckiest)
arr = arr[::-1]
for ind in range(len(new)):
    unluckiest += arr[ind] * new[ind]
print(luckiest, unluckiest)