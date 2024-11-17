class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for index, num in enumerate(nums):
            if index%2 == 1:
                for i in range(nums[index-1]):
                    ans.append(num)
        return ans
        