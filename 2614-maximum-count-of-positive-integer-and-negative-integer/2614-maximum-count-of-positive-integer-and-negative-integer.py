class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def brute_force(self, nums: List[int]) -> int:
            # TC: O(N)
            # SC: O(1)
            count_positive = 0
            count_negative = 0
            for num in nums:
                if num > 0:
                    count_positive +=1
                elif num < 0:
                    count_negative +=1
            return max(count_positive, count_negative)
        
        def binary_search(self, nums: List[int]) -> int:
            # hint: use bisect left and bisec right
            # lower bound(0)-1 to find last neg 
            l, r = 0, len(nums)-1
            last_neg = len(nums)
            
            while l <= r:
                mid = (l+r)//2
                if nums[mid] >= 0:
                    last_neg = mid
                    r = mid -1
                else:
                    l = mid + 1
            
            # upper bound(0) to find first pos
            l, r = 0, len(nums)-1
            first_pos = len(nums)

            while l <= r:
                mid = (l+r)//2
                if nums[mid] > 0:
                    first_pos = mid
                    r = mid -1
                else:
                    l = mid +1
            
            return max(last_neg, len(nums) - first_pos)
        return binary_search(self, nums)