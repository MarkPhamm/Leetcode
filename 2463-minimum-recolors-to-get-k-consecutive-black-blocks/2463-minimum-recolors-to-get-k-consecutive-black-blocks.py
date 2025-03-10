class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = math.inf
        white = 0

        for r, char in enumerate(blocks):
            if char == "W":
                white +=1
            if r < k - 1:
                continue
            l = r - k + 1
            if l > 0 and blocks[l-1] == "W":
                white -=1
            ans = min(white, ans)
        return ans
            

            

            

        