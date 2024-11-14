t = int(input())
arr = []
ss = set()
for _ in range(t):
    val = list(map(int, input().split(" ")))
    arr.append((val[0], val[1]))
ss = set(arr)
ss.difference()
cp = 0
# visited = set()
for ind in range(len(arr)):
    a, b = arr[ind][0], arr[ind][1]
    for sec in range(ind+1, len(arr)):
        c, d = arr[sec][0], arr[sec][1]
        x, y = (a+c)//2, (b+d)//2
        # print(a,c, b, d)
        # print(((a+c)//2, (b+d)//2))        
        if (x,y) in ss and (x,y) != (c,d) and (x,y) != (a,b) and abs(x-a) == abs(c-x) and abs(y-d) == abs(y-b):

            cp +=1
print(cp)