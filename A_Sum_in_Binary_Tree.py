def sum_in_binary_tree(n):
    current_vertex = 1
    total_sum = 0
    while n >= current_vertex:
        total_sum += current_vertex
        if n == current_vertex:
            break
        if n % 2 == 0:  # n is even
            current_vertex *= 2
        else:  # n is odd
            current_vertex = (current_vertex * 2) + 1
        n //= 2
    return total_sum

t = int(input())
for _ in range(t):
    n = int(input())
    result = sum_in_binary_tree(n)
    print(result)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
