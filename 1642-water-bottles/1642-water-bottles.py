class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles // numExchange > 0:
            ans += numBottles//numExchange
            numBottles = numBottles//numExchange + numBottles % numExchange
        return ans
            
        