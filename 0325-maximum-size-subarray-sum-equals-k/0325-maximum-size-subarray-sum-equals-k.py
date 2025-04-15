class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        for n in nums[1:]:
            prefix.append(n + prefix[-1])
        
        hashmap = {}
        hashmap = {0: -1}  # add base case for subarray starting at index 0
        max_len = 0

        for i in range(len(nums)):
            if prefix[i] - k in hashmap:
                max_len = max(max_len, i - hashmap[prefix[i] - k])
            if prefix[i] not in hashmap:
                hashmap[prefix[i]] = i

        return max_len
