s = input()
low = 0
up = 0
for i in range(len(s)):
    if s[i] >= 'A' and s[i] <= 'Z':
        up += 1
    else:
        low += 1
if up > low:
    print(s.upper())
elif low > up:
    print(s.lower())
else:
    print(s.lower())
