n = int(input())
arr = list(map(int, input().split(" ")))
odd = 0
even = 0

for i in range(len(arr)):
    if arr[i]%2 == 0:
        even +=1
    else:
        odd +=1

for i in range(len(arr)):
    if arr[i]%2 == 0 and odd > even:
        print(i+1)
        break
    elif arr[i] %2 != 0 and even > odd:
        print(i+1)
        break