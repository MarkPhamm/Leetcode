class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        # [[1,3],[2,6],[8,10],[15,18]
        for interval in intervals[1:]:
            last_interval = ans[-1]
            if interval[0] <= last_interval[1]: # case of overlap
                last_interval[1] = max(last_interval[1], interval[1])
            else:
                ans.append(interval)
        return ans 