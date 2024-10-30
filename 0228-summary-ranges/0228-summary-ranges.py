class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        i = 0
        j = 0
        results = []
        while i < n:
            if i < n-1:
                if nums[i]+1 != nums[i+1]:
                    if j == i:
                        results.append(str(nums[j]))
                    else:
                        results.append(str(nums[j]) + "->" + str(nums[i]))
                    j = i+1
                i+=1
            else:
                if j == i:
                    results.append(str(nums[j]))
                    break
                else:
                    results.append(str(nums[j]) + "->" + str(nums[i]))
                    break
        return results
                
