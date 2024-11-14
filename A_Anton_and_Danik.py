n = int(input())
inputString = input()
anton = inputString.count('A')
if n - anton == anton:
    print("Friendship")
elif n - anton < anton:
    print("Anton")
else:
    print("Danik")