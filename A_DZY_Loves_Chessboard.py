n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(input()))  # Convert input to list for modification

# Fill the board based on (i + j) parity
for i in range(n):
    for j in range(m):
        if arr[i][j] == ".":  # Only modify good cells
            arr[i][j] = "W" if (i + j) % 2 == 0 else "B"

# Print the result
for row in arr:
    print("".join(row))
