t = int(input())
for _ in range(t):
    n = int(input())
    # hi man
    val = input()
    stack = []
    for i in val:
        stack.append(i)
    cp = 0
    print(stack)
    stack = stack[::-1]
    while stack:
        if stack and stack[-1] == "0":
            cp +=1
            while stack and stack[-1] == '0':
                stack.pop()
        else:
            stack.pop()
    
    print(cp)