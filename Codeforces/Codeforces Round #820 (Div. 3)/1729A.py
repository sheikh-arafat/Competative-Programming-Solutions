t = int(input())
for test in range(t):
    eleOne = 0
    eleTwo = 0
    a, b, c = map(int,input().split())
    if a == 1:
        eleOne = 0
    else:
        eleOne = abs(a - 1)
    if c == 1:
        eleTwo = abs(b - 1)
    else:
        eleTwo = abs(b - c) + abs(c - 1)
    if eleOne < eleTwo:
        print(1)
    elif eleOne > eleTwo:
        print(2)
    else:
        print(3)
