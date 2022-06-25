n, m, a = map(int,input().split())
if n%a == 0:
    r1 = n//a
else:
    r1 = n//a + 1
if m%a == 0:
    r2 = m//a
else:
    r2 = m//a + 1
print(r1*r2)
