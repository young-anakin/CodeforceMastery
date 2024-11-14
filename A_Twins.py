n = int(input())
arr = list(map(int, input().split(" ")))

arr.sort()

x = 0

sm = sum(arr)
arr = arr[::-1]
# print(arr, "SUm : ", sm)
for ind in range(n):
    x += arr[ind]
    sm -= arr[ind]
    if x > sm:
        break

print(ind+1)