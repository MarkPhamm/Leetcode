class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
            highest = 0
            second_highest = 0

            for num in nums:
                if num > second_highest:
                    if num > highest:
                        second_highest = highest
                        highest = num
                    else:
                        second_highest = num
            if highest >= 2*second_highest:
                return nums.index(highest)
            else:
                return -1












        # sort_nums = nums.copy()
        # sort_nums.sort(reverse=True)
        # print(nums)
        
        # if sort_nums[0] >= 2*sort_nums[1]:
        #     print(sort_nums[0])
        #     return(nums.index(sort_nums[0]))
        # else:
        #     return -1