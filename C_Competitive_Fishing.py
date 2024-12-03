t = int(input())
for _ in range(t):
    num_fishes, min_diff = map(int, input().split())
    fishes = input().strip()

    
    score_differences = []
    total_diff = 0
    
    for i in range(num_fishes - 1, -1, -1):
        score_differences.append(total_diff)
        if fishes[i] == '1':
            total_diff += 1
        else:
            total_diff -= 1
    
    score_differences.reverse()
    
    current_diff = 0
    result = -1
    
    for num_groups in range(2, num_fishes + 1):
        current_diff += score_differences[num_groups - 2]
        if current_diff >= min_diff:
            result = num_groups
            break
    
    print(result)
