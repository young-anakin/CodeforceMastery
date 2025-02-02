def solve():
    n, k = map(int, input().split())  # Read n and k
    arr = list(map(int, input().split()))  # Read the array
    
    if n == k:
        # Case when n == k: Only check even indices (0-based)
        newarr = []
        for ind in range(len(arr)):
            if ind %2 == 0:
                newarr.append(arr[ind])
        newarr.append(0)
        # print(newarr)
        x = 0
        for i in range(0, len(newarr)):  # Only check even indices (i.e., 0, 2, 4, ...)
            if newarr[i] != i + 1:
                print(i + 1)  # Output the first index (1-based) where arr[i] != i + 1
                return
        print(1)  # If no mismatch found in even indices, print 1
    
    else:
        # Case when n > k: Flip the logic
        size = n
        limit = k
        hasDifferent = False
        
        # Check the first (size - limit + 1) elements to see if they differ from 1
        for i in range(1, size - limit + 2):  # Adjust index for Python (0-indexed)
            if arr[i] != 1:
                hasDifferent = True
                break
        
        if hasDifferent:
            print(1)
        else:
            print(2)

# Read number of test cases
t = int(input())
for _ in range(t):
    solve()
