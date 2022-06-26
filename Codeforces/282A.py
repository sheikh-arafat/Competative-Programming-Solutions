n = int(input())
out = 0
for i in range(n):
    bit = input()
    if '++' in bit:
        out += 1
    elif '--' in bit:
        out = out - 1
print(out)