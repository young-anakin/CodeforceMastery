val = input()
temp1 = val[0]
temp2 = val[1:]
if len(val) == 1:
    if val.islower():
        print(val.upper())
    else: 
        print(val.lower())
elif val.isupper() or val[0].islower() and val[1:].isupper():
    if val[0].islower():
        print(val[0].upper() + val[1:].lower())
    else:
        print(val.lower())
else:
    print(val)