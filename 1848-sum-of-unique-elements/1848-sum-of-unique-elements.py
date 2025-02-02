class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # TC: O(N)
        # SC: O(1)

        # hashmap = {}
        # for num in nums:
        #     hashmap[num] = hashmap.get(num, 0)+1
        
        # ans = 0
        # for key, value in hashmap.items():
        #     if value == 1:
        #         ans += key
        
        # return ans

        return sum(num for num in nums if nums.count(num) == 1)
        