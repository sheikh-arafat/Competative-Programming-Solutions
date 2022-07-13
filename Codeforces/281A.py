inp = input()

if inp[0] >= "a" and inp[0] <= "z" :
    inpZero = ord(inp[0])
    inpZero = inpZero - 32
    inpZero = chr(inpZero)
    out = inpZero + inp[1:]
    print(out)
else :
    print(inp)
