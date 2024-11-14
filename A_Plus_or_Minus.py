n = int(input())
for ind in range(n):
    a, b , c = list(map(int, input().split(" ")))
    if a + b == c:
        print("+")
    else: 
        print("-")