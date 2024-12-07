t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))

    stack = []

    def checkParity(a, b):
        if a % 2 == b % 2:
            return True
        else:
            return False
    cp = 0
    for ind in arr:
        if stack:
            if checkParity(stack[-1], ind):
                x = stack.pop()
                stack.append(x * ind)
                cp +=1
            else:
                stack.append(ind)
        else:
            stack.append(ind)
    print(cp)