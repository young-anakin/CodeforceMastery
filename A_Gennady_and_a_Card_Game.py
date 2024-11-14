val = input()
arr = list(map(str, input().split(" ")))
fl = False
for pp in arr:
    if val[0] in pp or val[1] in pp:
        fl = True
        break
if fl:
    print("YES")
else:
    print("NO")
# print(val, arr)