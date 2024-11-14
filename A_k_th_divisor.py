n, k = list(map(int, input().split(" ")))

i = 1
cp = 0
ans = -1
arr = []
while i * i <= n:
    # print(n/i)
    if n/i == int(n/i):
        arr.append(int(i))
        # cp +=2
    i +=1

other = []
for ind in arr:
    other.append(n//ind)

# print(other)
other = other[::-1]
arr.extend(other)
print(arr)
if k > len(arr):
    print(-1)
else:
    print(arr[k-1])
# if k > len(arr):
#     print(arr[k-1] * 2)
# else:
#     print(arr[k-1])