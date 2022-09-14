n = int(input())
l_count = 0
count = 0
while n > 0:
    ni = n % 10
    if ni == 4 or ni == 7:
        l_count += 1
    n = n // 10
if l_count == 0:
    print('NO')
else:
    while l_count > 0:
        nj = l_count % 10
        if nj != 4 and nj != 7:
            count += 1
        l_count = l_count // 10
    
    if count > 0:
        print('NO')
    else:
        print('YES')
