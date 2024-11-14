n = int(input())
count = 1
arr = []
for i in range(n):
    val = input()
    arr.append(val)
for a in range(n-1):
    if arr[a] != arr[a+1]:
        count +=1

print(count)