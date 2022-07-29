nStone = int(input())
colors = input()
c = 0
for i in range(len(colors)-1) :
    if colors[i] == colors[i+1] :
        c += 1 
print(c)
