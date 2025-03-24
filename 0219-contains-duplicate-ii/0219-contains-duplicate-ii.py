class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for index, char in enumerate(nums):
            if char in hashmap:
                if index - hashmap[char] <= k:
                    return True
                else:
                    hashmap[char] = index
            hashmap[char] = index
        return False
