class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(i for i in range(1,10))
        ans = []

        def backtrack(curr, curr_sum):
            if curr_sum == n and len(curr) == k:
                ans.append(curr[:])
                return
            elif curr_sum > n or len(curr) > k:
                return

            else:
                for candidate in candidates:
                    if curr and candidate <= curr[-1]:
                        continue
                    curr_sum += candidate
                    curr.append(candidate)
                    backtrack(curr, curr_sum)
                    curr_sum -= curr[-1]
                    curr.pop()
            
        backtrack([], 0)
        return ans
