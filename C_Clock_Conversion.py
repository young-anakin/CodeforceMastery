n = int(input())
for ind in range(n):
    val = input()

    hr = val[0:2]
    mn = val[3:]

    if int(hr) >= 0 and int(hr) < 12:
        t = "AM"
    else:
        t = "PM"

    if int(hr) >= 12:
        hr =  int(hr) - 12
        hr = str(hr)
    if str(hr) == "00" or str(hr) == "0":
        hr = "12"

    if len(str(hr)) == 1:
        hr = "0" + str(hr)

    fin = hr + ":" + mn + " " + t

    print(fin)