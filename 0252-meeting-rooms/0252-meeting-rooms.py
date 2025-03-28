class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        last_end = 0
        for meeting in intervals:
            if meeting[0] < last_end:
                return False
            last_end = meeting[1]
        return True
        