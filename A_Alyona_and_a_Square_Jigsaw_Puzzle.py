t = int(input())
def generate_sequence(start, increment, count):
    """
    Generate a sequence of numbers starting from a given value, 
    incrementing by a fixed amount, for a specified count.

    Parameters:
    start (int): The starting value of the sequence.
    increment (int): The difference between consecutive terms.
    count (int): The number of terms to generate.

    Returns:
    list: The generated sequence as a list.
    """
    return [start + increment * i for i in range(count)]

# Example usage:
start_value = 1
increment_value = 7
number_of_terms = 10000

sequence = generate_sequence(start_value, increment_value, number_of_terms)
print(sequence)

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))

    days = sequence
    sm = 0
    j = 0
    cp = 0
    for ind in range(n):
        sm += arr[ind]
        # print(sm, days[j])
        if sm == days[j]:
            cp +=1
            j +=1
            sm = 0
        while sm > days[j]:
            j +=1
    
    print(cp)

