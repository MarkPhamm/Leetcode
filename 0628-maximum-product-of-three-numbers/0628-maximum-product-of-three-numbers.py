class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product_a = nums[-1] * nums[-2] * nums[-3]
        product_b = nums[-1] * nums[0] * nums[1]
        return max(product_a, product_b)
        