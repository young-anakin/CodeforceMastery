a = int(input())
b = int(input())
c = int(input())
ans = 0
arr = []

arr.append(a+b+c)
arr.append(a*b*c)
arr.append(a+(b*c))
arr.append(a * (b+c))
arr.append((a+b)*c)
arr.append((a*b)+c)
print(max(arr))