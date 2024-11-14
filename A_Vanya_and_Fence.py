SizeAndHeight = list(map(int, input().split(' ')))
Size = SizeAndHeight[0]
Height = SizeAndHeight[1]
count = 0
heightLists = list(map(int, input().split(' ')))
for i in range(0, Size):
    if heightLists[i] > Height:
        count += 1
# print(count)
print(count * 2 + (Size- count))
