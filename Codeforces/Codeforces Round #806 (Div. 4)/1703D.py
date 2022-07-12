t = int(input())
for i in range(t):
    n = int(input())
    m_list = []
    n_list = []
    for p in range(n):
        inp = input()
        m_list.append(inp)
    n_list = m_list
    for j in range(len(n_list)):
        cur = n_list[j]
        count = 0
        for i in range(len(cur)):
            sub_cur = cur[:i+1]
            post_cur = cur[i+1:]
            for s in n_list:
                if cur != s:
                    if sub_cur == s:
                        count += 1
                        break
            if count == 1:
                for s1 in n_list:
                    if cur != s1:
                        if post_cur == s1:
                            count += 1
                            break
            if count == 2:
                break
            else:
                count = 0
        if j == n-1:
            if count == 2:
                print(1)
            else:
                print(0)
        else:
            if count == 2:
                print(1,end="")
            else:
                print(0,end="")
