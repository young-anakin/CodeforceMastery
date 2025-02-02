val = input()
val2 = input()

if val == val2:
    print(-1)
else:
    print(max(len(val), len(val2)))