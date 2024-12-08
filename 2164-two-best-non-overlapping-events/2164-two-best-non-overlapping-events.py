class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ends = sorted(events, key=lambda x: x[1])
        starts = sorted(events, key=lambda x: x[0])
        max_val = 0
        end_idx = 0
        res = 0

        for i in range(len(starts)):
            while end_idx < len(ends) and ends[end_idx][1] < starts[i][0]:
                max_val = max(max_val, ends[end_idx][2])
                end_idx += 1
            
            res = max(res, starts[i][2] + max_val)
        
        return res
