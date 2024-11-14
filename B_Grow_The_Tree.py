n = int(input())
li = list(map(int, input().split(" ")))
li.sort()
last = n//2
sum1 = 0
sum2 = 0
for ind in range(last):
    sum1 += li[ind]

li = li[last:]
for ind in range(len(li)):
    sum2 += li[ind]

sum1 = pow(sum1, 2)
sum2 = pow(sum2, 2)
print(sum1 +  sum2)


