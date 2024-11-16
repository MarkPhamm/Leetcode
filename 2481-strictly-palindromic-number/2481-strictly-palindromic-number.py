class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base(n, base):
            palindrome = ""
            while n!= 0:
                palindrome += str(n%base)
                n = n//base
            return palindrome.strip() == palindrome.strip()[::-1]

        for i in range(2, n-1):
            if to_base(n, i) == False:
                return False
        return True