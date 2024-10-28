class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        j = 0
        n = len(nums)
        results = []
        while i <= n-1:
            if i == n-1:
                if j == i:
                    results.append(str(nums[j]))
                else:
                    results.append(str(nums[j])+"->"+str(nums[i]))
                break
            elif nums[i+1] == nums[i]+1:
                i+=1
            else:
                if j == i:
                    results.append(str(nums[j]))
                else:
                    results.append(str(nums[j])+"->"+str(nums[i]))
                i+=1
                j=i
        return results