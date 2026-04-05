class Solution:
    def trap(self, height: List[int]) -> int:
        left_arr = [] # [0,1,1,2,2,2,2,3,3,3,3,3] find the left biggest 
        right_arr = [] # [3,3,3,3,3,3,3,3,2,2,2,1] find the right biggest 

        left_max = 0
        right_max = 0

        ans = 0

        n = len(height)

        for i in range(n):
            left_max = max(left_max, height[i])
            left_arr.append(left_max)

            right_max = max(right_max, height[n-i-1])
            right_arr.append(right_max)
        
        right_arr = right_arr[::-1]
        
        
        for i in range(len(left_arr)):
            potential_water = min(left_arr[i], right_arr[i])
            ans += (potential_water - height[i])
        
        return ans 
        

            