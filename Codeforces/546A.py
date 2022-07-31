k, n, w = map(int,input().split())
for i in range(w):
    n = n - (i+1)*k
if n < 0:
    print(abs(n))
else:
    print(0)
