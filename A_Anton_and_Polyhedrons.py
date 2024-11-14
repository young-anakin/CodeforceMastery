di = {"Icosahedron" : 20, "Cube" : 6, "Tetrahedron" : 4, "Dodecahedron":12, "Octahedron" : 8}
n = int(input())
fin = 0
for i in range(n):
    ans = input()
    fin += di[ans]

print(fin)