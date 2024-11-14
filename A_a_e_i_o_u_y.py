vowel = "aeiouy"
n = int(input())
val = input()
stack = []
for ind in range(n):
    if val[ind] not in vowel:
        stack.append(val[ind])
    else:
        if not stack:
            stack.append(val[ind])
        else:
            if stack[-1] not in vowel:
                stack.append(val[ind])
print( "".join(stack))