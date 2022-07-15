t = int(input())
for p in range(t):
    n, x = map(int,input().split())
    height_arr = list(map(int,input().split()))
    height_arr.sort()
    half = len(height_arr) // 2
    first = height_arr[:half]
    last = height_arr[half:]
    for q in range(half):
        res = first[q] + x
        if last[q] >= res:
            first[q] = 0
            last[q] = 0
    if sum(first) ==0 and sum(last) == 0:
        print("YES")
    else:
        print("NO")
