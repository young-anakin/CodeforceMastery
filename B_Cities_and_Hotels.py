n, d = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
ss = set()
import bisect
xx = sorted(arr)
# print(xx)
for ind in range(n):
    ss.add(arr[ind])
mx, mn = max(arr), min(arr)
cp = 0
for ind in range(n):
    x = d + arr[ind]
    y = arr[ind] - d
    # print(x, y)
    first = bisect.bisect_left(xx, x)
    if x not in ss:
        # print("x is ", x, first)
        if x >= mx:
            if abs(mx - x) >= d:
                cp +=1
                ss.add(x)
                # print("ya")
        else:
            if abs(arr[first] - x) >= d and abs(arr[first-1] - x) >= d:
                cp +=1
                ss.add(x)
                # print("ya")

    second = bisect.bisect_left(xx, y)
    if y not in ss:
        # print("Y is ", y, second)
        if y >= mx:
            if abs(mx - y) >= d:
                cp +=1
                ss.add(y)
                # print("ya")

        else:
            if abs(arr[second] - y) >= d and abs(arr[second-1] - y) >= d:
                cp +=1
                ss.add(y)
                # print("ya")


print(cp)