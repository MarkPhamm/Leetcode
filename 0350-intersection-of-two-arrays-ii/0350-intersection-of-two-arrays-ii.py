from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def hashmap(self, nums1: List[int], nums2: List[int]) -> List[int]:
            # TC: O(n)
            # SC: O(n)
            hashmap = dict(Counter(nums1))
            ans = []

            for num in nums2:
                if num in hashmap and hashmap[num] > 0:
                    ans.append(num)
                    hashmap[num] -= 1
            return ans
        
        def two_pointer(self, nums1: List[int], nums2: List[int]) -> List[int]:
            # TC: O(n log n)
            # SC: O(1)
            nums1.sort()
            nums2.sort()
            i, j = 0, 0
            ans = []

            while i < len(nums1) and j < len(nums2):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    i+=1
                    j+=1
                elif nums1[i] > nums2[j]:
                    j+=1
                else:
                    i+=1
            return ans

        def binary_search(self, nums1: List[int], nums2: List[int]) -> List[int]:
            # TC: O(n log n)
            # SC: O(1)
            nums1.sort()
            nums2.sort()
            ans = []
            
            def binary_search(target, nums):
                """Finds the leftmost occurrence of target in nums using binary search."""
                index = bisect.bisect_left(nums, target)
                if index < len(nums) and nums[index] == target:
                    return index
                return -1
            
            for num in nums1:
                index = binary_search(num, nums2)
                if index != -1:
                    ans.append(num)
                    nums2.pop(index)  # Remove used element to avoid duplicate counting
        
            return ans
        return binary_search(self, nums1, nums2)