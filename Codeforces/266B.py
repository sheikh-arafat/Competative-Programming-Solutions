n, t = map(int,input().split())
s = input()
sList = []
for iStr in s:
    sList.append(iStr)
print(sList)
# tmp = ""
# for i in range(t):
#     j = 0
#     while j<n:
#         if s[j] == "B" and s[j+1] == "G":
#             s[j], s[j+1] = s[j+1], s[j]
#             j += 1
#         j += 1
