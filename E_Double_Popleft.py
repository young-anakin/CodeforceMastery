n, size = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
mx = max(arr)
i = arr.index(mx)
# print(mx, i)
from collections import defaultdict
dd = defaultdict(int)


from collections import deque
sub = deque()
for ind in range(0, i):
    sub.append(arr[ind])

print(sub)
new = []
# for ind in range(i+1):
#     if arr[ind] <= arr[ind+1]:
#         sub.append(arr[ind])
#     else:
a = 0
while len(sub) != 1:
    if sub[0] <= sub[1]:
        tmp = sub.popleft()
        new.append(tmp)
    else:
        tmp = sub.popleft()
        tmp2 = sub.popleft()
        new.append(tmp2)
        sub.appendleft(tmp)
print(sub)
new.append(sub[0])

print(arr)
sub = arr[0:i]



new = arr[i+1:] + new   
fin = len(new)
print(new)


# print(new)
for ind in range(size):
    ans = int(input())
    if ans >= i+1:
        print(mx, new[((ans-n)%fin)])
    else:   
        print(new[ans-1], )