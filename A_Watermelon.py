def waterMelon(n):
    if n == 2:
        return "No"
    if n%2 != 0:
        return "No"
    return "Yes"


n = int(input())
print(waterMelon(n))