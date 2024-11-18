t = int(input())
def transpose_array(arr):
    # Transpose using list comprehension
    return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
for _ in range(t):
    arr = []

    for _ in range(8):
        arr.append(input())
    
    print(arr)
    
    # Check for a full red row ('R') first
    fl = False
    for row in arr:
        if row == "R" * 8:
            fl = True
            break
    
    x = transpose_array(arr)
    for row in x:
        if row == "R" * 8:
            fl = True
            break
    if fl:
        print("R")
    else:
        print("B")
    # print(x)
    # else:
    #     # If no full red row, blue must be the last one
    #     print("B")
