def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary if binary else "0"

# Example usage
decimal_number = 13005955444444444444444444444444444444444444444444444444444444444444444444444
binary_representation = decimal_to_binary(decimal_number)
print(binary_representation)
