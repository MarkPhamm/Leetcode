class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        ans = 0
        for k in range(n):
            goal = target - nums[k]
            i = k + 1
            j = n - 1
            while i < j:
                if nums[i] + nums[j] < goal:
                    ans += j-i
                    i+=1
                else:
                    j-=1
        return ans

        