x = int(input())
summ = 0
a = 1
cp = 0
while summ <= x:
    val = int((a * (a+1))/2)
    summ += val
    cp +=1
    a +=1
print(cp-1)
    
