n = int(input())
capacity = 0
maxCapacity = 0
for i in range(0, n):
    inputList = list(map(int, input().split(" ")))
    capacity -= inputList[0]
    capacity += inputList[1]
    if maxCapacity < capacity:
        maxCapacity = capacity
print(maxCapacity)