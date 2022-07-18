t = int(input())
for tests in range(t):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    s = []
    s_out = ""
    for apnd in range(m):
        s.append('B')
    for i,el in enumerate(a):
        alt = (m + 1) - el
        if el < alt:
            if s[el-1] == 'A':
                s[alt-1] = 'A'
            else:
                s[el-1] = 'A'
        else:
            if s[alt-1] == 'A':
                s[el-1] = 'A'
            else:
                s[alt-1] = 'A'
    print(s_out.join(s))
