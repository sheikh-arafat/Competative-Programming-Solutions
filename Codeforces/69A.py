n = int(input())
xi = yi = zi = 0
for i in range(n):
    a = list(map(int,input().split()))[:3]
    xi = xi + a[0]
    yi = yi + a[1]
    zi = zi + a[2]
print('YES') if (xi == 0 and yi ==0 and zi == 0) else print('NO')
