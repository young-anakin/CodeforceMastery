n = int(input())
m = int(input())
arr = []
for ind in range(n):
    val = int(input())
    arr.append(val)

arr.sort()
arr.reverse()
cp = 0
vol = 0
for ind in range(len(arr)):
    vol += arr[ind]
    cp += 1
    if vol >= m:
        break
print(cp) 