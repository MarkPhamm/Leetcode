# from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def bisect_left(nums, target):
            l,r = 0, len(nums)-1
            ans = len(nums)
            
            while l <= r:
                mid = (l+r)//2
                if nums[mid] >= target:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
        
        ans = []
        for spell in spells:
            target = success/spell
            ans.append(len(potions)-bisect_left(potions, target))
        return ans
