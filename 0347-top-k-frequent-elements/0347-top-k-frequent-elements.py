class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        arr = []
        for n, cnt in count.items():
            arr.append([cnt,n])
        
        arr.sort(reverse = True)

        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans

        print(arr)

        # print(frequency)
        