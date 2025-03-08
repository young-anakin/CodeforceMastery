n = int(input())
stack = []
val = input()
for i in val:
    stack.append(i)
    while len(stack) > 1:
        if stack[-1] != stack[-2]:
            stack.pop()
            stack.pop()
        else:
            break

print(len(stack))