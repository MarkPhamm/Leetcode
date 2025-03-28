class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        hashmap = {}

        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                j = stack.pop()
                hashmap[j] = p 
            stack.append(i)
            
        return [prices[i] - hashmap.get(i, 0) for i in range(len(prices))]