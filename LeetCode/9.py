class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum = 0
        temp = x
        while x > 0 :
            sum = (sum * 10) + (x % 10)
            x = x // 10
        return temp == sum
