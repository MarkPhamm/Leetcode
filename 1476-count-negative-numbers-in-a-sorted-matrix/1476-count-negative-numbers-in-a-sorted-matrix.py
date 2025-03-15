class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # def find_first_negative_index(arr):
        #     low, high = 0, len(arr) - 1
        #     result = -1  # Initialize with an invalid index

        #     while low <= high:
        #         mid = (low + high) // 2
        #         if arr[mid] < 0:
        #             result = mid  # Found a negative number, so we record the index
        #             high = mid - 1  # Move left to check if there's another negative number
        #         else:
        #             low = mid + 1  # Move right because current element is non-negative

        #     return result

        # return sum(len(row) - find_first_negative_index(row) 
        #         if find_first_negative_index(row) >= 0 
        #         else 0 
        #         for row in grid)
        ans = 0
        for row in grid:
            for num in row:
                if num < 0:
                    ans+=1
        return ans

