class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)
        for cur in range(0, n):
            next = 0 if cur == n-1 else cur+1
            prev = cur - 1
            if (colors[next] == colors[prev]) and colors[prev] != colors[cur]:
                ans +=1
        return ans
        