values = list(map(int, input().split(" ")))
total = 0
for i in range(1, values[2]+1):
    # print(values[0], i)
    total += values[0] * i

# print(total)
# print(values[1])
answer = total - values[1]
if answer < 0:
    print(0)
else:
    print(total - values[1])
