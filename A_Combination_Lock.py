n = int(input())  # Number of disks
initial_state = input()  # Initial state of the disks
combination = input()  # Desired combination

# Function to calculate the minimum number of moves for a single disk
def min_moves_for_disk(initial_digit, target_digit):
    clockwise_moves = (target_digit - initial_digit + 10) % 10
    counterclockwise_moves = (initial_digit - target_digit + 10) % 10
    return min(clockwise_moves, counterclockwise_moves)

# Calculate total moves required by summing up moves for each disk
total_moves = sum(min_moves_for_disk(int(initial_state[i]), int(combination[i])) for i in range(n))

print(total_moves)
