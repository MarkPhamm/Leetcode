class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        arr1 = []
        arr2 = []
        for num in set1:
            if num not in set2:
                arr1.append(num)
        
        for num in set2:
            if num not in set1:
                arr2.append(num)

        return [arr1,arr2]