class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def brute_force(self, arr: List[int], k: int) -> int:
            i = 1
            ans = []
            while len(ans) != k:
                if i not in arr:
                    ans.append(i)
                i+=1
            print(ans)
            return ans[k-1] 

        def binary_search(self, arr: List[int], k: int) -> int:
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                missing = arr[mid] - (mid + 1)

                if missing < k:
                    left = mid + 1  # Move right
                else:
                    right = mid - 1  # Move left

            return left + k  # Formula to find the missing number



        return binary_search(self, arr, k)