n = int(input())
arr = list(map(int, input().split(" ")))

ans = 0

a = 1

sz = (n//2)+1
arr.sort()
while a < sz:
    # print(arr[-a], arr[a])
    vl = (arr[-a] + arr[a-1])
    ans += pow(vl,2)
    a+=1
print(ans)



