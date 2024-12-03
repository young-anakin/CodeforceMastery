def solve():
    # Read inputs
    n, b, c = map(int, input().split())
    
    if b == 0:
        if c + 2 < n:
            print("-1")
            return
        elif c + 1 == n or c + 2 == n:
            print(n - 1)
            return
        else:
            print(n)
            return
    
    if c >= n:
        print(n)
        return
    
    # Calculate number of steps
    num = (n - c) // b
    if num * b + c == n:
        num -= 1
    
    # Output result
    print(n - (num + 1))

# Driver code to handle multiple test cases
t = int(input())  # Number of test cases
for _ in range(t):
    solve()
