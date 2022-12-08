y = int(input())
y2 = y+1
while y2 > y:
    test = y2
    yArr = []
    ySet = set()
    while test > 0:
        rem = test % 10
        test = test // 10
        yArr.append(rem)
        ySet.add(rem)
    if len(yArr)==len(ySet):
        break
    else:
        y2 = y2 + 1
print(y2)
