str_i = input()
length = len(str_i)
players = 0
out = 'NO'
for i in range(length):
    if i != length-1:
        if str_i[i+1] == str_i[i]:
            players += 1
        else:
            players = 0
        if players >= 6:
            out = 'YES'
print(out)
