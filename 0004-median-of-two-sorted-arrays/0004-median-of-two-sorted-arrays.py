class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        upper = ceil((len(num)+1)/2)
        lower = floor((len(num)+1)/2)   

        return (num[upper-1]+num[lower-1])/2
        