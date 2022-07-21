user = input()
arr = []

for i in range(len(user)) :
    if user[i] not in arr:
        arr.append(user[i])
length = len(arr)
if length % 2 == 0 :
    print("CHAT WITH HER!")
else :
    print("IGNORE HIM!")
