n = int(input())
for i in range(n):
    x = str(input())
    print(x[0] + str(len(x)-2) + x[-1]) if len(x) > 10 else print(x)