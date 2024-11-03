class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalpha() or char.isnumeric()).lower()
        print(s)
        return s == s[::-1]