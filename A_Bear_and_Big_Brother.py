li = list(map(int, input().split(' ')))
year_count = 0
LimakWeight = li[0]
BobWeight = li[1]
while LimakWeight <= BobWeight:
    LimakWeight *= 3
    BobWeight *= 2
    year_count +=1
print(year_count)