s = input()
t = input()
new = ""
for el in s:
    new = el + new
if t == new:
    print('YES')
else:
    print('NO')
