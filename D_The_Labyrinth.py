def binary_search_condition(low, high, condition):
    while low < high:
        mid = low + (high - low) // 2
        if condition(mid):
            high = mid
        else:
            low = mid + 1
    return low