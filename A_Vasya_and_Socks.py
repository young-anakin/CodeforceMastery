val1 = input()
val2 = input()
def inbound(i, j):
  return i >= 0 and j >= 0 and i < len(val1) and j < len(val2)

new = [[[] for ind in range(len(val2)+1)] for j in range(len(val1)+1)]
print(new)
fin = ""
for ind in range(0, len(val1)):
  for j in range(0, len(val2)):
    if val1[ind] == val2[j]:
        new[ind+1][j+1].append(new[ind][j].append(val1[ind])) 
    else:
        if len(new[ind+1][j]) >= len(new[ind][j+1]):
            new[ind+1][j+1].append(new[ind+1][j])
        else:
            new[ind+1][j+1].append(new[ind][j+1]) 
           

print(new)
print(fin)
      