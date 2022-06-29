inpt = input()
vowels = ['a','e','i','o','u','y']
for i in inpt:
    if i.lower() in vowels:
        inpt = inpt.replace(i,"")
inpt = inpt.lower()
outL = ""
for i in range(len(inpt)):
    out = "."+inpt[i]
    outL = outL+out
print(outL)
