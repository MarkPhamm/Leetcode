class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        n = len(nums)

        for k in range(n-2):
            if k > 0 and nums[k] == nums[k - 1]:  # Skip duplicates for k
                continue
            i = k+1
            j = n-1
            target = -nums[k]

            while i < j:
                if nums[i] + nums[j] == target:
                    ans.add((nums[k],nums[i],nums[j]))
                    i+=1
                    j-=1

                elif nums[i] + nums[j] > target:
                    j-=1
                else:
                    i+=1
                    
        return [list(t) for t in ans] 
        