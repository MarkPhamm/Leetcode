class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp_bottom_up(cost):
            n = len(cost)
            dp = [0] * (n+1)

            for i in range(2,n+1):
                dp[i] = min( dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            return dp[-1]
        
        def dp_top_down(cost):
            cache = {0:0, 1:0}
            n = len(cost)
            def min_cost(i):
                if i in cache:
                    return cache[i]
                else: 
                    cache[i] = min(
                            cost[i-1] + min_cost(i-1), 
                            cost[i-2] + min_cost(i-2)
                            )
                    return cache[i]
            return min_cost(n)
        return dp_top_down(cost)