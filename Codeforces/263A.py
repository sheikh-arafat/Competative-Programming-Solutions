col = 0
row = 0
for i in range(5):
    a1 = input().split()
    if '1' in a1:
        col = a1.index('1') + 1
        row = i + 1
move = abs(3 - col) + abs(3 - row)
print(move)