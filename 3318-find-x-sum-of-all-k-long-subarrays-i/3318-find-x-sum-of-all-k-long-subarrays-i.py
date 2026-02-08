class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n-k+1):
            hashmap = {}
            sub_array = nums[i:i+k]
            
            for char in sub_array: 
                hashmap[char] = hashmap.get(char, 0) + 1
            
            # sort the hashmap by value 
            hashmap_sorted = dict(sorted(hashmap.items(), key = lambda x: (-x[1], -x[0])))

            j = 0
            cur = 0  
            for key, value in hashmap_sorted.items():
                if j == x:
                    break
                cur += key*value
                j += 1
            ans.append(cur)
        return ans 