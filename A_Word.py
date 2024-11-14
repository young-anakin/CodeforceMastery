inputString = input()
Small = 0
Capital = 0
for index in range(0, len(inputString)):
    if 65 <= ord(inputString[index]) <= 90:
        Capital += 1
    else:
        Small += 1

if Capital <= Small:
    print(inputString.lower())
else:
    print(inputString.upper())