class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        while True:
            if nums and nums[-1] >= k:
                nums.pop()
            else:
                break
        return len(nums)
            