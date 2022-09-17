n = int(input())
total = cap = 0 
for i in range(n):
    a, b = map(int, input().split())
    total -= a
    total += b
    cap = max(total, cap)
print(cap)
