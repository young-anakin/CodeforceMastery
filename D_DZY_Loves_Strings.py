word = input()
sz = int(input())
arr = list(map(int, input().split(" ")))
mx = max(arr)
dd = {}
for ind in range(26):
    dd[chr(97+ind)] = arr[ind]
# print(dd)
sm = 0
for ind in range(len(word)):
    sm += dd[word[ind]] * (ind+1)
vl = len(word)
for ind in range(sz):
    sm += (vl+1) * mx
    vl +=1 
print(sm)

