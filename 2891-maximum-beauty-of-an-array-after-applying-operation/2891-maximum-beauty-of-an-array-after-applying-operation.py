class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()  # Step 1: Sort the array
        max_beauty = 0
        start = 0
        
        for end in range(len(nums)):  # Step 2: Expand the end pointer
            # Step 3: Check the condition and adjust the start pointer
            while nums[end] - nums[start] > 2 * k:
                start += 1
            # Step 4: Update the maximum beauty
            max_beauty = max(max_beauty, end - start + 1)
        
        return max_beauty