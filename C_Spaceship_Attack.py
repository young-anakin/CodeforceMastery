s, b = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
chance = []
ps = [0]
sub = []
for ind in range(b):
    val = list(map(int, input().split(" ")))
    sub.append(val)
sub.sort(key = lambda x: x[0])
for ind in range(len(sub)):
    chance.append(sub[ind][0])
    ps.append(ps[-1] + sub[ind][1])
# ps.pop(0)
# print(ps, chance)
import bisect
final = []
for ind in range(s):
    val = bisect.bisect_right(chance, arr[ind] )
    final.append(ps[val])

print(" ".join(map(str, final)))