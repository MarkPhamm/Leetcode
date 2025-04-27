class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            arr = nums[i:i+3]
            print(arr)
            if (arr[0] + arr[2])*2 == arr[1]:
                ans +=1
        return ans