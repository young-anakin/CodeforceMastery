import sys

# Function to send a query to the interactor
def query(a, b):
    print(f"? {a} {b}", flush=True)  # Send the query to the interactor
    return int(input())  # Get the response from the interactor

a = 1
for ind in range(1, 51):
    res = query(ind+1, ind)
    res2 = query(ind, ind+1)


    if res == -1:
        print(f"! {ind-1}", flush = True)
        break
    
    if res == res2:
        continue
    else:
        print(f"! {res + res2}")
        break