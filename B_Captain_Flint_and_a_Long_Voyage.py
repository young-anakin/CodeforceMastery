from collections import defaultdict
dd = defaultdict(int)
ans = []
for ind in range(1, 10):
    dd[ind] = bin(ind)[2:]
    if len(bin(ind)[2:]) == 1:
        ans.append(bin(ind)[2:])
    elif len(bin(ind)[2:]) == 2:
        ans.append(bin(ind)[2:]) 
    elif len(bin(ind)[2:]) == 3:
        ans.append(bin(ind)[2:])
    else:
        ans.append(bin(ind)[2:])

# print(dd)
t = int(input())
for ind in range(t):
    arr = []

    n = int(input())
    x = ""
    cp = 0
    total = 4*n
    emikeyer = total - n
    for ind in range(n):
    # for j in range(4):
        # arr.append(ans[8][j])
        cp += 4
        if cp > emikeyer:
            x += "8"
        else:
            x += "9"
        # x += ans[8]
        # arr.append(ans[8])
    print(x)
    # print(arr)

#     i = 1
#     while i != n+1:
#         arr[-i] = '0'
#         i +=1

#     fin = ""
#     stk = []
#     for ind in range(len(arr)):
#         stk.append(arr[ind])

#         if len(stk) == 4:
#             x = "".join(stk)
#             stk = []
#             if str(int(x, 2)) == "0":
#                 fin += "8"
#             else:
#                 fin += str(int(x, 2))

#     # print(arr)
#     print(fin)
# # print(ans)    