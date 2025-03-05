class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 0
        for i in range(1,2*(n-1),2):
            ans+= 2*i
        ans += 2*n-1
        return ans