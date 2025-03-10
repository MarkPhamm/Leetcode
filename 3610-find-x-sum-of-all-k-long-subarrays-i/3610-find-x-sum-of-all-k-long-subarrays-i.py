class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        def return_value(my_dict, x):
            sorted_dict = sorted(my_dict.items(), key=lambda item: (-item[1], -item[0]))
            top_x = sorted_dict[:x]
            result = sum(key * value for key, value in top_x)
            return result
        
        cnt = defaultdict(int)
        for i in range(k):
            cnt[nums[i]]+=1
        ans.append(return_value(cnt, x))

        l = 0 
        for r in range(k, len(nums)):
            cnt[nums[r]] +=1
            cnt[nums[l]] -=1
            l+=1
            ans.append(return_value(cnt, x))
        return ans

        