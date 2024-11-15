class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # place_hold = []
        # ans = []
        # for num in nums:
        #     if num in place_hold:
        #         ans.append(num)
        #     else:
        #         place_hold.append(num)

        # return ans
        map = {}
        ans = []
        for num in nums:
            map[num] = map.get(num,0) + 1
        
        for num, count in map.items():
            if count == 2:
                ans.append(num)
        
        return ans
        

        