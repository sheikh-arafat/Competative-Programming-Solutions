inp = input()
arr = []
out = ""
if "+" in inp :
    arr = inp.split("+")
    arr = [int(i) for i in arr]
    n = len(arr)
    for i in range(n) :
        for j in range(0, n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for i in range(n-1) :
        outStr = str(arr[i]) + "+"
        out = out + outStr
    out = out + str(arr[-1])
    print(out)
else :
    print(inp)
