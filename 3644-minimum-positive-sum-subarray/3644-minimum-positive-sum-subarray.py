class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # TC: O((r - l + 1) * n) ≈ O(n²)
        # SC: O(1)
        n = len(nums)
        ans = math.inf

        for length in range(l, r+1):
            
            if length > n: # handling edge case length > len(nums)
                continue

            # calculating initial window sum
            window_sum = sum(nums[:length])
            print(window_sum) 
            if window_sum > 0:
                ans = min(ans, window_sum)

            # sliding window approach
            for i in range(length, n):
                window_sum += nums[i] - nums[i-length]
                print(window_sum)
                if window_sum > 0:
                    ans = min(ans, window_sum)
        
        return ans if ans < math.inf else -1
            


        
        