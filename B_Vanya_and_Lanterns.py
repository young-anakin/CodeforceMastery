# Input number of lamp posts and length of the street
n, l = map(int, input().split())

# Input the positions of the lamp posts
arr = list(map(int, input().split()))

# Sort the positions of the lamp posts
arr.sort()
print(arr)
# Calculate the maximum initial distance from either end of the street
d = 2 * max(arr[0], l - arr[n - 1])
print(d)
# Calculate the maximum distance between consecutive lamp posts
for i in range(1, n):
    d = max(d, (arr[i] - arr[i - 1]))

# Calculate and print the minimum radius required for complete coverage
# with a precision of 9 decimal places
print(f"{d / 2:.9f}")
