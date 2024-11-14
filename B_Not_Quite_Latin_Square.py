n = int(input())
final = "ABC"
for ind in range(n):
    new = []
    for j in range(3):
        arr = input()
        if '?' in arr:
            if "A" in arr and "C" in arr:
                print("B")
            elif "B" in arr and "C" in arr:
                print("A")
            else:
                print("C")
        