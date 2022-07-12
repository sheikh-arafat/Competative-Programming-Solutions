t = int(input())
for i in range(t):
    n = int(input())
    n_list = list(map(int,input().split()))[:n]
    for j in range(n):
        cur = n_list[j]
        mn, moves = input().split()
        num = int(mn)
        for i in moves:
            if i == "D":
                cur += 1
            else:
                cur -= 1
                
            if cur == 10:
                cur = 0
            elif cur == -1:
                cur = 9
        if j == n-1:
            print(cur)
        else:
            print(cur,end=" ")
