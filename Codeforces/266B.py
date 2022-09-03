n, t = map(int,input().split())
s = input()
sList = []
for iStr in s:
    sList.append(iStr)
for i in range(t):
    j = 0
    while j<n:
        if j != n-1 and sList[j] == "B" and sList[j+1] == "G":
            sList[j], sList[j+1] = sList[j+1], sList[j]
            j += 1
        j += 1
for e in sList:
    print(e, end ="")
