def build_segment_tree(data):
    n = len(data)
    tree = [0] * (2 * n)

    # Insert leaf nodes in the segment tree
    for i in range(n):
        tree[n + i] = data[i]

    # Build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
    
    return tree

def update_segment_tree(tree, n, index, value):
    pos = index + n
    tree[pos] = value

    # Update the parent nodes
    while pos > 1:
        pos //= 2
        tree[pos] = tree[2 * pos] + tree[2 * pos + 1]

def range_query(tree, n, left, right):
    # Query the sum in the range [left, right)
    left += n
    right += n
    sum_val = 0

    while left < right:
        if left % 2 == 1:
            sum_val += tree[left]
            left += 1
        if right % 2 == 1:
            right -= 1
            sum_val += tree[right]
        left //= 2
        right //= 2

    return sum_val
