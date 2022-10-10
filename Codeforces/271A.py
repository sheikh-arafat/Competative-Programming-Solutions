y = int(input())
temp = y+1
say = True
while say == True:
    arrT = []
    temp2 = temp
    while temp > 0:
        rem = temp % 10
        arrT.append(rem)
        temp = temp // 10
    
    for i in range(len(arrT)):
        k= i+1
        for j in range(k, len(arrT)):
            if arrT[i] == arrT[j]:
                say = True
                break
                break
            else:
                say = False
    temp2 += 1
print(temp2)
