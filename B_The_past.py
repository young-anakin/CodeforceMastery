n, m = list(map(int, input().split(" ")))  # Input for n and m
a = list(map(int, input().split(" ")))  # Sequence a
b = list(map(int, input().split(" ")))  # Sequence b

b.sort()  # Sort b in descending order to maximize the chance of breaking monotonicity

for ind in range(n):
    if a[ind] == 0:
        a[ind] = b.pop()  # Replace zeros in a with elements from b

# print(sorted(a), a)
if sorted(a) == a:  # Check if a is still strictly increasing
    print("No")
else:
    print("Yes")
