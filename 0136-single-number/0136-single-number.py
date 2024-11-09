class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        for num, count in counter.items():
            if count == 1:
                return num
        