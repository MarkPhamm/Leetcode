class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        
        left_most = n
        l, r = 0, n-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= target:
                left_most = mid
                r = mid -1
            else:
                l = mid +1

        right_most = n
        l, r = 0, n-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] > target:
                right_most = mid
                r = mid -1
            else:
                l = mid +1

        print(right_most)
        return (right_most - left_most) > n/2
