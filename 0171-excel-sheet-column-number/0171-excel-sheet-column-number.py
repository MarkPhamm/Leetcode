class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        hashmap = {chr(i): i - 64 for i in range(65, 91)}

        columnTitle_reverse = columnTitle[::-1]
        ans = 0
        for index, char in enumerate(columnTitle_reverse):
            ans += hashmap[char] * (26**(index))
        return ans