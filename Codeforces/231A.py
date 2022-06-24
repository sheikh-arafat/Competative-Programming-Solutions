n = int(input())
count = 0
for i in range(n):
    arr = input().split()
    if int(arr[0]) + int(arr[1]) + int(arr[2]) > 1:
        count += 1
print(count)