from bisect import bisect_left
n = int(input())

tot = 0
last = 1
while tot < n:
    tot += (last*(last+1))/2
    # print(tot)
    last +=1

if tot > n:

    print(last-2)
else:
    print(last-1)


