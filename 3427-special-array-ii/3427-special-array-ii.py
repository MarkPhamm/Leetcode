class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        def isOdd(num):
            return num%2==1

        def isEven(num):    
            return num%2==0
            
        # Handle edge case where nums has only one element
        if len(nums) == 1:
            # For single-element subarrays, all queries return True
            return [True for _ in queries]

        helper = []    
        for i in range(len(nums)-1):
            if (isOdd(nums[i]) & isOdd(nums[i+1])) or (isEven(nums[i]) & isEven(nums[i+1])):
                helper.append(False)
            else:
                helper.append(True)
        
        # Step 2: Create prefix sum for `False` counts in helper
        prefix_false_count = [0] * len(helper)
        prefix_false_count[0] = 0 if helper[0] else 1
        for i in range(1, len(helper)):
            prefix_false_count[i] = prefix_false_count[i - 1] + (0 if helper[i] else 1)
        
        print(prefix_false_count, helper)
        # Step 3: Process queries efficiently
        ans = []
        for fromi, toi in queries:
            if toi - fromi == 0:  # Single-element subarray
                ans.append(True)
            else:
                # Check range [fromi, toi-1] in helper using prefix sum
                false_count = prefix_false_count[toi - 1] - (prefix_false_count[fromi - 1] if fromi > 0 else 0)
                ans.append(false_count == 0)

        return ans