class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
            if hashmap[n] == 2:
                return True
        return False 