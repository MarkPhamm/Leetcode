class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reverse_nums = []
        for num in nums:
            reverse_num = int(''.join(list(str(num)[::-1])))
            reverse_nums.append(reverse_num)

        return len(set(nums+reverse_nums))
