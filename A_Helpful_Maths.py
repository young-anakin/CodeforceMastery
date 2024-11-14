def HelpfulMaths(arr):
    val = ""
    arr.sort()
    for a in arr:
        val += str(a) + "+"
    return val[0:-1]

values = list(map(int, input().split('+')))
print(HelpfulMaths(values))