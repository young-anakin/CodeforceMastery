arr = list(map(int, input().split(" ")))
arr.sort()
# print(arr)
x = arr[0]
y = arr[1]
z = arr[2]
b = int((z - (x+y))/-2)
a = x - b
c = z - a
print(a, b, c)