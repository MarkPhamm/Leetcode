class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_abs = math.inf
        ans = []

        for i in range(1, len(arr)):
            min_abs = min(abs(arr[i] - arr[i-1]), min_abs)

        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) == min_abs:
                ans.append([arr[i-1], arr[i]])
        return ans