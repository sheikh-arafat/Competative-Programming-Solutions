class Solution:
    def maxInstance(self, s : str) -> int:
        # code here
        b = a = l = o = n = 0
        for i in s :
            if i == 'b' :
                b += 1
            elif i == 'a' :
                a += 1
            elif i == 'l' :
                l += 1
            elif i == 'o' :
                o += 1
            elif i == 'n' :
                n += 1
        l //= 2
        o //= 2
        return min(b, min(a, min(l, min(o, n))))
