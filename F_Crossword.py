n = int(input())
s = input()

starter = None
count = 0

ans = []

index = 0
while index < n:
    if s[index] == "B":
        starter = "B"
        break
    index += 1

for i in range(index, n):
    if s[i] == starter:
        count += 1
    else:
        if count:
            ans.append(count)
            count = 0
if count:
    ans.append(count)

print(len(ans))
print(*ans)