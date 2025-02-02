class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # a: [1,2,3,0,0,0]
        #               i    
        # b: [2,5,6]
        #         j



        # []
        # [1,2,2,3,5,6]
        
        # two pointer method like merge sort from the bottom of nums1, nums2
        # Compare nums1[i], nums2[j], which one is larger then deducted it by 1, and add to nums1
        # Until nums1 or num2 is empty

        # Two pointer (Reader pointer)
        i, j = m - 1, n - 1

        # Additional pointer to insert the merges number in (Writer pointer)
        k = m + n - 1 

        # While there's still element in the list
        while i >= 0 and j >= 0:
            # compare
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                # move i pointer
                i -= 1
            else:
                nums1[k] = nums2[j]
                # move j pointer
                j -= 1
            # move k to write the next element
            k -= 1

        # copy the rest of j
        while j>=0:
            nums1[k] = nums2[j]
            j-=1
            k-=1


