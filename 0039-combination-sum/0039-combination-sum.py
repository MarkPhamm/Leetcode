class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(curr, curr_sum):
            if curr_sum == target:
                ans.append(curr[:])
                return
            elif curr_sum > target:
                return

            else:
                for candidate in candidates:
                    if curr and candidate < curr[-1]:
                        continue
                    curr_sum += candidate
                    curr.append(candidate)
                    backtrack(curr, curr_sum)
                    curr_sum -= curr[-1]
                    curr.pop()
            
        backtrack([], 0)
        return ans
