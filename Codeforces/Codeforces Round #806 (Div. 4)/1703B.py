t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    s_list = []
    s_str = ""
    for i in s:
        if i in s_list:
            s_str = s_str + i
        else:
            s_list.append(i)
    total = len(s_str) + 2 * len(s_list)
    print(total)
