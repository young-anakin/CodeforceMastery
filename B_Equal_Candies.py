# Function to calculate the minimum candies to eat
def min_candies_to_eat(n, candies):
    total_candies = sum(candies)
    avg_candies = total_candies // n  # Integer division to get the average

    candies_to_eat = 0
    for candy_count in candies:
        if candy_count > avg_candies:
            candies_to_eat += candy_count - avg_candies

    return candies_to_eat

# Input processing
t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    
    result = min_candies_to_eat(n, candies)
    print(result)
