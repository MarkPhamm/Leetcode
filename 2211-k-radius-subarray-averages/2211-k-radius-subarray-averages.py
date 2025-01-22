class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_sum = 0
        window_size = 2*k + 1
        ans = [-1] * n 

        if n < window_size:
            return ans

        for i in range(window_size):
            window_sum += nums[i]

        for i in range(k, n - k):
            ans[i] = window_sum // window_size
            if i + k + 1 < n: 
                window_sum += nums[i + k + 1]
            window_sum -= nums[i - k]

        return ans