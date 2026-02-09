class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        prefix = []
        postfix = []

        for num in nums:
            if not prefix:
                prefix.append(num)
            else:
                prefix.append(prefix[-1]*num)
        
        for num in nums[::-1]:
            if not postfix:
                postfix.append(num)
            else:
                postfix.append(postfix[-1]*num)
        postfix = postfix[::-1]
        print(prefix, postfix)

        for i in range(len(nums)):
            if i == 0:
                left = 1
                right = postfix[i+1]
            elif i == len(nums) - 1:
                left = prefix[i-1]
                right = 1 
            else: 
                left = prefix[i-1]
                right = postfix[i+1]
            ans.append(left*right)
        
        return ans 
                