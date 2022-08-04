t = int(input())
for test in range(t):
    mins = 0
    n = int(input())
    if n == 0:
        mins = 0
    elif n == 1 or n == -1:
        mins = 2
    elif n == 2 or n == 3 or n == -2 or n == -3:
        mins = 1
    elif n == 4 or n == -4:
        mins = 2
    elif n % 3 == 0:
        mins = min((n//3),(n//2))
    else:
        mins = (n//3) + 1
    print(abs(mins))
