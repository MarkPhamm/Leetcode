class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = math.inf
        white = 0

        for i in range(k):
            if blocks[i] == "W":
                white +=1
        ans = white

        for r in range(k, len(blocks)):
            if blocks[r] == "W":
                white +=1
            if blocks[r-k] == "W":
                white -=1
            ans = min(white, ans)
        return ans
            

            

            

        