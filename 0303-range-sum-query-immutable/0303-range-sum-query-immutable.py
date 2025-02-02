# Prefix Sum Question
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # create attribute prefix sum
        # SC: O(n)
        # TC: O(n)
        self.prefix_sum = [0]
        for num in self.nums:
            self.prefix_sum.append(num + self.prefix_sum[-1])
        
    def sumRange(self, left: int, right: int) -> int:
        # TC: O(right-left)
        # SC: O(1)
        # current_sum = 0
        # for i in range(left, right+1):
        #     current_sum+=self.nums[i]
        # return current_sum

        # TC: O(1)
        # SC: O(1)
        # sum range = prefix(r+1) - prefix(l) become O(1)
        return self.prefix_sum[right+1] - self.prefix_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)