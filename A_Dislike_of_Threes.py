arr = []
n = int(input())
beg = 1
ind = 0
while ind <= 1000:
    if beg %3 != 0 and str(beg)[-1] != '3':
        arr.append(beg)
        ind +=1
    beg +=1
for ind in range(n):
    x = int(input())
    print(arr[x-1])
