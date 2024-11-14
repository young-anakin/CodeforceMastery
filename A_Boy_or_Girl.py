value = input()
unique = []
for i in range(0, len(value)):
    if value[i] not in unique:
        unique.append(value[i])
    
print("CHAT WITH HER!" if len(unique)%2 == 0 else "IGNORE HIM!")