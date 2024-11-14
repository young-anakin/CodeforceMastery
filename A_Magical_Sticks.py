n = int(input())
indexList = []
frequency = {}
for a in range(0, n):
    indexList.append(int(input()))
    frequency[indexList[-1]] = 1
# print(frequency)
for a in range(0, n):
    for b in range(a+1, n):
        if indexList[a] + indexList[b] in frequency:
            # print(indexList[a] + indexList[b])
            frequency[indexList[a]+indexList[b]] +=1
answer = [] 
for values in frequency.values():
    print(values)
