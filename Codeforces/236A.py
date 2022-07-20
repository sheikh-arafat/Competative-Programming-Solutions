inp = input()
inp = dict.fromkeys(inp)  # Convert it to dictionary to remove duplicates.
 
if len(inp) % 2 == 0 :
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
