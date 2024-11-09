class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_arr = []
        for i  in nums_set:
            nums_arr.append(i)
        nums_arr.sort(reverse = True)
        print(nums_arr)

        if len(nums_arr) <= 2:
            return(nums_arr[0])
        else:
            return(nums_arr[2])