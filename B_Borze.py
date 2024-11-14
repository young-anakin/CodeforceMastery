val = input()

one = "."
two = "-."
three = "--"
a = 0
n = len(val)-1
ans = ""
while a <= n:
    if val[a] == ".":
        ans += "0"
        a +=1
    elif val[a] == "-":
        if val[a+1] == "-":
            ans += "2"
        else:
            ans += "1"
        a +=2
print(ans)