def Petya(str1, str2):
    new1 = ""
    new2 = ""
    for a in range(0, len(str1)):
        if ord(str1[a]) < 92:
            new1 += str1[a] + 32
        else:
            new1 += str1[a]
        if ord(str2[a]) < 92:
            new2 += str2[a] + 32
        else:
            new2 += str2[a]        
    if new1<new2:
        return -1
    elif new1>new2:
        return 1
    return 0

str1 = input()
str2 = input()
print(Petya(str1, str2))