n = int(input())
for ind in range(n):
    chest, key , stamina = list(map(int, input().split(" ")))
    if chest < key: 
        chest += stamina
        if chest >= key:
            print(key)
        else:
            print(chest  + (key - chest)*2)
    else:
        print(chest)
        