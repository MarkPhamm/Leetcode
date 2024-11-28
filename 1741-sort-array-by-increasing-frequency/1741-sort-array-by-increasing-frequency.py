class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0)+1
        
        counter_bucket = {}
        for number, occur  in counter.items():
            if occur not in counter_bucket:
                counter_bucket[occur] = [number]
            else:
                counter_bucket[occur].append(number)
        
        ans_arr = []
        for occur, bucket in counter_bucket.items():
            bucket.sort(reverse = True)
            ans_arr.append([occur, bucket])
        
        ans_arr.sort()
        
        ans = []
        for pair in ans_arr:
            for num in pair[1]:
                ans.extend([num] * pair[0])
        return ans
        
        

        