n = 3
arr = []
for ind in range(n):
    x = input()
    arr.append(x)


ans = []
for r in range(len("abc")):
    for c in range(n):
        candidates = []
        candidates.append(arr[r][c]) 
        if c+1 <= 2:
            candidates.append(arr[r][c+1]) 
        if r-1 >=0 and c+1 <= 2:
            candidates.append(arr[r-1][c+1]) 
        if r-1 >= 0:
            candidates.append(arr[r-1][c])
        if r-1 >= 0 and c -1 >= 0:
            candidates.append(arr[r-1][c-1])
        if c-1 >= 0:
            candidates.append(arr[r][c-1]) 
        if r+1 <= 2 and c-1 >= 0:  
            candidates.append(arr[r+1][c-1]) 
        if r+1 <= 2:
            candidates.append(arr[r+1][c]) 
        if r+1 <=2 and c+1 <=2:
            candidates.append(arr[r+1][c+1])
        ans.append(candidates)
    # candidates.sort()
    print(candidates)




