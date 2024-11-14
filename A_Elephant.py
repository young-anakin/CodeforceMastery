value = int(input())
if value <=5:
    print(1)
elif value%5 == 0:
    print(int(value/5))
else:
    print(value//5 + 1)