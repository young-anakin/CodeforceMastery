def checker(arr, k, b):
    gain = 0
    loss = 0
    for ind in range(len(arr)):
        val = b-arr[ind]
        if val < 0:
            loss += val
        else:
            gain += val
        
    tot = gain + loss
    return (k/100) * loss <= tot


n, k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

r = max(arr)
l = 0

while l + 10**-6 <= r:
    md =(l+r)/2    
    if checker(arr, k, md):
        r = md
    else:
        l = md
print(md)


