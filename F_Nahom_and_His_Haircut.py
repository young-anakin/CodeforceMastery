import sys
from collections import Counter

def can_cut_hair(n, a, b, m, x):
    # Step 1: Immediate invalid case
    for i in range(n):
        if a[i] < b[i]:  # Impossible case
            return "NO"

    # Step 2: Count the required razor sizes
    required_cuts = Counter()
    stack = []  # Stack to track active valid cuts
    
    7 9 4 5 3 3 3 6 8 10 3 2 5
    5 3 1 5 3 2 2 5 8 5 1 1 5
    for i in range(n):
        while stack and stack[-1] < b[i]:
            stack.pop()  # Remove invalid cuts
        
        if stack and stack[-1] == b[i]:
            continue  # Already a valid cut exists
        
        if a[i] > b[i]:  # We need to cut
            required_cuts[b[i]] += 1
            stack.append(b[i])  # Push the required razor
    
    # Step 3: Count available razors
    available_razors = Counter(x)
    
    # Step 4: Ensure we have enough razors for the required cuts
    for size in required_cuts:
        if required_cuts[size] > available_razors[size]:
            return "NO"
    
    return "YES"

# Read input
input = sys.stdin.read
data = input().split()
index = 0
t = int(data[index])
index += 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n
    b = list(map(int, data[index:index + n]))
    index += n
    m = int(data[index])
    index += 1
    x = list(map(int, data[index:index + m]))
    index += m
    
    results.append(can_cut_hair(n, a, b, m, x))

sys.stdout.write("\n".join(results) + "\n")
