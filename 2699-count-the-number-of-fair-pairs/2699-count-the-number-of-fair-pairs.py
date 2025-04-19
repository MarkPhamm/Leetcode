class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # count = P(X <= 6) - P(X <= 2)
        # find P(X<= target)
        nums.sort()
        def count_lower(threshold):
            count = 0
            l = 0 
            r = len(nums) -1    
            while l < r:
                if nums[l] + nums[r] > threshold:
                    r -=1 
                else:
                    count += r-l
                    l+=1
            return count
        return count_lower(upper) - count_lower(lower-1)


        