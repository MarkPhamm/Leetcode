class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums)+1)]
        
        # Initiate the count
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        # sort the count into buckets, each buckets as the number of occurence
        for n, cnt in count.items():
            frequency[cnt].append(n)

        ans = []
        for i in range(len(frequency)-1, 0,-1):
            for n in frequency[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
    
