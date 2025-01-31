class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]  # Start with 0 for handling index 0 properly

        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)  # Build prefix sum array

        total_sum = prefix_sum[-1]  # Total sum of all elements

        for i in range(len(nums)):
            left_sum = prefix_sum[i]  # Sum of elements before index i
            right_sum = total_sum - prefix_sum[i+1]  # Sum of elements after index i
            
            if left_sum == right_sum:
                return i  # Return the leftmost index that satisfies the condition

        return -1  # No valid index found