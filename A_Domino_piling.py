def Domino(arr):
    return (arr[0] * arr[1])//2


arr = list(map(int, input().split(" ")))
print(Domino(arr))