class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        threshold = n/2 
        
        hashmap = {}
        for n in nums: 
            hashmap[n] = hashmap.get(n, 0) + 1
            if hashmap[n] >= threshold:
                return n 
    