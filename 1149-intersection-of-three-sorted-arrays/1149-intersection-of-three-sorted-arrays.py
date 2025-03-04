from typing import List

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        def set_sol(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
            # TC: O(n log n)
            # SC: O(n)
            set1 = set(arr1)
            set2 = set(arr2)
            set3 = set(arr3)
            return sorted(list(set1.intersection(set2).intersection(set3)))
        
        def hashmap(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
            # TC: O(n)
            # SC: O(n)
            hashmap = {}
            ans = []

            arr = arr1 + arr2 + arr3
            for num in arr:
                hashmap[num] = hashmap.get(num, 0) + 1
            
            for k, v in hashmap.items():
                if v == 3:
                    ans.append(k)
            
            return ans

        def binary_search(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
            # TC: O(n log n)
            # SC: O(1)
            def exists_in_array(arr, target):
                """Binary search helper function to check if target exists in arr."""
                left, right = 0, len(arr) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if arr[mid] == target:
                        return True
                    elif arr[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
            
            result = []
            for num in arr1:  # O(n)
                if exists_in_array(arr2, num) and exists_in_array(arr3, num):  # O(log n) each
                    result.append(num)  # O(1)
            
            return result

        return binary_search(self, arr1, arr2, arr3)
