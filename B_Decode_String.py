t = int(input())
abc = "abcdefghijklmnopqrstuvwxyz"
for _ in range(t):
    n = int(input())-1
    arr = input()
    val = []
    for ind in range(len(arr)):
        val.append(arr[ind])
    stack = []
    # print(val)
    while val:
        a = val.pop()
        if a != '0':
            stack.append(abc[int(a)-1])
        else:
            b = val.pop()
            c = val.pop()
            stack.append(abc[int(c+b)-1])
    ab = "".join(stack)
    print(ab[::-1])