class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def set_sol(self, nums1: List[int], nums2: List[int]) -> List[int]:
            set1 = set(nums1)
            set2 = set(nums2)
            return list(set1.intersection(set2))
        
        def binary_search(self, nums1: List[int], nums2: List[int]) -> List[int]:
            def check_exist(target, nums):
                nums.sort()
                l, r = 0, len(nums) - 1

                while l <= r:
                    mid = (l+r)//2
                    if nums[mid] == target:
                        return True
                    elif nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            
            ans = []
            for num in nums1:
                if check_exist(num, nums2) and num not in ans:
                    ans.append(num)
            return ans
        return binary_search(self, nums1, nums2)
