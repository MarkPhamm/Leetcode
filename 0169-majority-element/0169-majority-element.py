class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        
        for num, count in counter.items():
            if count > len(nums)/2:
                return num
        