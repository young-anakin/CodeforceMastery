r, b = list(map(int, input().split(" ")))
ogr, ogb = r, b
turn = False # True-petya, 
arr = []
pet, vas = 0,0
if b > r:
    arr.append("R")
    r -=1
else:
    arr.append("B")
    b -=1
while b != 0 or r != 0:
    if turn:
        if arr[-1] == "B":
            if b > 0:
                arr.append("B")
                b -=1
            else:
                arr.append("R")
                r -=1
        else:
            if r > 0:
                arr.append("R")
                r -=1
            else:
                arr.append("B")
                b -=1
        
    else:
        if arr[-1] == "R":
            if b > 0:
                arr.append("B")
                b -=1
            else:
                arr.append("R")
                r -=1
        else:
            if r > 0:
                arr.append("R")
                r -=1
            else:
                arr.append("B")
                b -=1
    
    turn = not(turn)
    # print(arr, b, r, turn)


# print("second")
turn = False
arr2 = []
b, r = ogb, ogr
if b > r:
    arr2.append("B")
    b -=1
else:
    arr2.append("R")
    r -=1

# print(r, b)
while b != 0 or r != 0:
    if turn:
        if arr2[-1] == "B":
            if b > 0:
                arr2.append("B")
                b -=1
            else:
                arr2.append("R")
                r -=1
        else:
            if r > 0:
                arr2.append("R")
                r -=1
            else:
                arr2.append("B")
                b -=1
        
    else:
        if arr2[-1] == "R":
            if b > 0:
                arr2.append("B")
                b -=1
            else:
                arr2.append("R")
                r -=1
        else:
            if r > 0:
                arr2.append("R")
                r -=1
            else:
                arr2.append("B")
                b -=1
    
    turn = not(turn)
    # print(arr, b, r, turn)



vas1, pet1 = 0,0
for ind in range(1, len(arr2)):
    if arr2[ind] == arr2[ind-1]:
        pet1 +=1
    else:
        vas1 +=1

for ind in range(1, len(arr)):
    if arr[ind] == arr[ind-1]:
        pet +=1
    else:
        vas +=1

# print(arr)
# print(arr2)
# print(pet1, vas1)
# print(pet, vas)
# print(arr, arr2)
# print(pet)
if pet1 > pet:
    print(pet1, vas1)
else:
    print(pet, vas)

# print(arr)
# print(arr2)
# print(pet, vas)