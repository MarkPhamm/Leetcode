class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def set_method(self, nums1: List[int], nums2: List[int]) -> int:
            # TC: O(n+m)
            # SC: O(n+m)
            nums1_set = set(nums1)
            nums2_set = set(nums2)
            intersection = nums1_set.intersection(nums2_set)
            return min(intersection)

        def two_pointer(self, nums1: List[int], nums2: List[int]) -> int:
            # TC: O(n+m)
            # SC: O(1)
            i,j = 0,0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] == nums2[j]:
                    return nums1[i]  # Return early since it's the smallest common element
                elif nums1[i] > nums2[j]:
                    j += 1
                else:
                    i += 1

            return -1  # No common element found
        return two_pointer(self, nums1, nums2)
        