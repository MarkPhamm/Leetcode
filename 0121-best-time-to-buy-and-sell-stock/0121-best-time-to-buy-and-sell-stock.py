class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        min = prices[0]
        max_gain = 0
        while i < len(prices):
            if prices[i] < min:
                min = prices[i]
            else:
                gain = prices[i] - min
                if gain > max_gain:
                    max_gain = gain
            i+=1
        return max_gain


        