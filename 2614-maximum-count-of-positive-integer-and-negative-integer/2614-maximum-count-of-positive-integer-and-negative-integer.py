class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def bisect_left(nums, target):
            """
            find the index when insert, all the numbers to it right is LARGER OR EQUAL to target
            Eg: bisect_right([-3,-2,-1,0,0,1,2],0) return 3
            """
            l,r = 0, len(nums)
            ans = len(nums)
            while l<r:
                mid = (l+r)//2
                if nums[mid] >= target:
                    ans = mid
                    r = mid
                else:
                    l = mid + 1
            return ans

        def bisect_right(nums, target):
            """
            find the index when insert, all the numbers to it right is LARGER THAN target
            Eg: bisect_right([-3,-2,-1,0,0,1,2],0) return 5, 
            from there, we can calculate the number of positive number by taking len(nums) - ans
            """
            l,r = 0, len(nums)
            ans = len(nums)
            while l<r:
                mid = (l+r)//2
                if nums[mid] > target:
                    ans = mid
                    r = mid
                else:
                    l = mid + 1
            return ans


        last_neg = bisect_left(nums, 0)
        first_pos = bisect_right(nums, 0)
        print(last_neg, first_pos)
        return max(last_neg, len(nums) - first_pos)
