n, m = list(map(int, (input().split(" "))))
fin = []
from collections import defaultdict
dd = defaultdict(tuple)
for _ in range(m):
    a, b = list(map(str, input().split(" ")))
    dd[a] = (b, 1)
    dd[b] = (a, 2)

s = list(map(str, input().split(" ")))
for word in s:
    # print(word, dd[word])
    if len(word) < len(dd[word]):
        fin.append(word)
    elif len(word) > len(dd[word][0]):
        fin.append(dd[word][0])
    else:
        if dd[word][1] == 1:
            fin.append(word)
        else:
            fin.append(dd[word][0])
# print(s)
print(" ".join(fin))