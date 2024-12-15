n, a, b = list(map(int, input().split(" ")))
arr = [ind+1 for ind in range(n)]*1000

# if b >= 0:
curr = a-1
i = 0

print(arr[curr + b])


        


# print(arr)