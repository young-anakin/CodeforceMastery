love = "I love"
hate = "I hate"
n = int(input())
if n == 1:
    print("I hate it")
else:
    strb = ""
    code = 1
    for ind in range(n):
        if ind %2 == 0:
            if ind == n-1:
                strb += "I hate it"
            else:
                strb += "I hate that "
        elif ind %2 == 1:
            if ind == n-1:
                strb += "I love it"
            else:
                strb += "I love that "
    print(strb)
    

