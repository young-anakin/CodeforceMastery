n , m = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
carry = 0
arr.sort()
for ind in range(n):
    if m > 0:
        if arr[ind] < 0:
            carry += abs(arr[ind])
            m-=1

print(carry)