n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Array to store the count of distinct numbers from index i to the end
distinct_count = [0] * n
seen = set()  # Set to track unique numbers

# Traverse the array from the end to the beginning
for i in range(n - 1, -1, -1):
    seen.add(arr[i])
    distinct_count[i] = len(seen)

# Handle the queries
results = []
for _ in range(m):
    l = int(input())
    results.append(distinct_count[l - 1])  # Convert 1-based to 0-based index

# Output results
print("\n".join(map(str, results)))
