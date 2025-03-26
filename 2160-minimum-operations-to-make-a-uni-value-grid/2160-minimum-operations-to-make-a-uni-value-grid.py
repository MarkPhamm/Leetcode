class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid_flatten = []
        for g in grid:
            grid_flatten.extend(g)
        grid_flatten.sort()
        
        median = grid_flatten[len(grid_flatten)//2]
        
        ans = 0
        
        for num in grid_flatten:
            if abs(num-median)%x != 0:
                return -1
            else:
                ans += int(abs(num-median)/x)
        return ans
        