class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}

        for n in nums2:
            while stack and n > stack[-1]:
                out = stack.pop()
                hashmap[out] = n
            stack.append(n)
        
        ans = []
        for n in nums1:
            if n in hashmap:
                ans.append(hashmap[n])
            else:
                ans.append(-1)
        return ans
