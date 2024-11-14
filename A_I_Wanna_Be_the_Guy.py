# Read input values
n = int(input())
x_levels = list(map(int, input().split()[1:]))
y_levels = list(map(int, input().split()[1:]))

# Create a set to store the levels that both Little X and Little Y can pass
all_levels = set(x_levels + y_levels)

# Check if the set of all levels covers all levels from 1 to n
if len(all_levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
