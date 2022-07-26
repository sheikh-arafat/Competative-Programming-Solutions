user = input()
arr = []
 
for i in range(len(user)) :
    count = 0
    for j in range(len(arr)) :
        if user[i] == arr[j] :
            count = count + 1
            break
    if count == 0 :
        arr.append(user[i])
length = len(arr)
if length % 2 == 0 :
    print("CHAT WITH HER!")
else :
    print("IGNORE HIM!")
