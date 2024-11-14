from collections import Counter
ans = input()
ans = ans[1:-1]
fin = ans.split(", ")
sub = Counter(fin)
if ans == "":
    print(0)
else:
    print(len(sub))
