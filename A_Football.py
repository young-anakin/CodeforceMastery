n = int(input())
a = int(input())
b = int(input())

winners = [0 for ind in range(n)]
losers = [0 for ind in range(n)]

chance = True
# for winners
for ind in range(n):
    if chance:
        if a != 0:
            winners[ind] +=1
            a -=1
        else:
            if b != 0:
                losers[ind] +=1
                b -=1
    else:
        if b != 0:
            losers[ind] +=1
            b -=1
        else:
            if a != 0:
                winners[ind] +=1
                a -=1
    
    chance = not(chance)
chance = False
for ind in range(n):
    if chance:
        if a != 0:
            winners[ind] +=1
            a -=1
        else:
            if b != 0:
                losers[ind] +=1
                b -=1
    else:
        if b != 0:
            losers[ind] +=1
            b -=1
        else:
            if a != 0:
                winners[ind] +=1
                a -=1
    
    chance = not(chance)
ind = 0

print(winners, losers, a, b)
for ind in range(len(losers)):
    if losers[ind] == winners[ind]:
        losers[ind] += b
        winners[ind] +=a

cp = 0        
for ind in range(n):
    if winners[ind] == losers[ind]:
        cp +=1

print(cp)
for ind in range(len(winners)):
    print(str(winners[ind]) + ":" + str(losers[ind]))

# print(winners, a)
# print(losers, b)