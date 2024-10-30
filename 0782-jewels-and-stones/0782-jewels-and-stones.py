class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        results = 0
        for i in stones:
            if i in jewels:
                results +=1
        return results
