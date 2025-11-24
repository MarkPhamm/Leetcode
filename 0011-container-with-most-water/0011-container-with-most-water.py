class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        max_area = 0
        while l < r:
            l_height = height[l]
            r_height = height[r]
            length = r - l
            area = min(l_height, r_height) * length
            max_area = max(area, max_area)
            if l_height < r_height: 
                l+=1
            else:
                r-=1
        return max_area