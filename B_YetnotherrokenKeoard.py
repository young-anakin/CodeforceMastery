n = int(input())
for ind in range(n):
    val = input()
    capital = []
    small = []

    for j in range(len(val)):
        if val[j] == "B":
            if len(capital) != 0:
                capital.pop()
        elif val[j] == "b":
            if len(small) != 0:
                small.pop()
        elif val[j] == val[j].lower():
            small.append((val[j], j))
        else:
            capital.append((val[j], j))
    capital.extend(small)
    capital.sort(key= lambda x: x[1])
    ans = ""
    for z in range(len(capital)):
        ans += capital[z][0]
    print(ans)
