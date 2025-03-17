class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for count in hashmap.values():
            if count%2 == 1:
                return False
        
        return True
        