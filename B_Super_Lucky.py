n = input()
x = len(str(n))
ans = ""
bucket = []
def ans(orig, val, four, seven):
    print(val)
    if len(val) == four *2:
        print(val)
        if int(val) <= orig:
            bucket.append(val)
    
    if four > 0:
        val += "4"
        four -=1
        ans(orig, val, four, seven)
        
        # four +=1
    
    if seven > 0:
        val += "7"
        seven -=1
        ans(orig, val, four, seven)
        # seven +=1
    return bucket

def ans2 (orig, val, four, seven, cp):  
    print(val)

    if len(val) == (cp):
        if int(val) <= orig:
            bucket.append(val)
        return
    
    if seven > 0:
        val += "7"
        seven -=1
        ans2(orig, val, four, seven, cp)
        # seven +=1
    if four > 0:
        val += "4"
        four -=1
        ans2(orig, val, four, seven, cp)
        
        # four +=1
    

    return bucket
    
print(x//2)    
print(ans(4500, "", x//2, x//2 ))
print(ans2(4500, "", x//2, x//2, x))




# if x %2 != 0:
#     new = x+1
#     for ind in range(new//2):
#         ans += "4"
#     for ind in range(new//2):
#         ans += "7"
#     print(ans)
# else:
#     mn = ""
#     mx = ""

#     for ind in range(x//2):
#         mn += "4"
#         mx += "7"
#     for ind in range(x//2):
#         mx += "4"
#         mn += "7"

#     new = x+2
#     if int(n[0]) > int("7"):
#         for ind in range(new//2):
#             ans += "4"
#         for ind in range(new//2):
#             ans += "7"
#         print(ans)
#     elif int(n[0]) < int("4"):
#         for ind in range(x//2):
#             ans += "4"
#         for ind in range(x//2):
#             ans += "7"
#         print(ans)  
#     else:
#         if int(mn) >= int(n):
#             print(int(mn))
#         elif int(mx) >= int(n):
#             print(int(mx))
#         else:
#             print("hi")





            
        