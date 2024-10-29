
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max_gain = 0
        i = 0
        n = len(prices)

        while i < n:
            gain = prices[i] - min
            if prices[i] < min:
                min = prices[i]
            if gain > max_gain:
                max_gain = gain
            i+=1
        return max_gain


        