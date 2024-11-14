from collections import defaultdict
def color(arr):
    id = ['M', "C", "Y"]
    for ind in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[ind][j] in id:
                return "#Color"
    return "#Black&White"

size = list(map(int, input().split(" ")))
arr = []
for ind in range(size[0]):
    val = list( input().split(" "))
    arr.append(val)
print(color(arr))