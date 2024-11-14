n = int(input())
ans = 0
cp = 0
arr = list(map(int, input().split(" ")))
for ind in range(n):
    if arr[ind] > 0:
        cp += arr[ind]
    elif arr[ind] == -1:
        if cp <= 0:
            ans +=1
        else:
            cp -= 1
print(ans)


# n = int(input())
# ans = 0
# cp = 0
# arr = list(map(int, input().split(" ")))

# for ind in range(n):
#     if arr[ind] > 0:
#         cp += arr[ind]
#     elif arr[ind] == -1:
#         if cp <= 0:
#             ans += 1
#         else:
#             cp -= 1

# print(ans)