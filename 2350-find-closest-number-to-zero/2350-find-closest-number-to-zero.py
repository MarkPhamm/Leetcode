class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distance = abs(nums[0])
        closest_num = nums[0]
        for i in range(len(nums)):
            if abs(nums[i]) < distance:
                distance = abs(nums[i])
                closest_num = nums[i]
            elif abs(nums[i]) == distance:
                if nums[i] > closest_num:
                   closest_num = nums[i]
        return closest_num

        